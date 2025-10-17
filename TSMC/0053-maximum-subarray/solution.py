'''
[-2, 1,-3,4,-1,2,1,-5,4]
 -2, 1, 1,4, 4,5,6, 4,4
dp[0] = [-2]
dp[1] = max(dp[0], []+1, 1) = 1, [1]
dp[2] = max(dp[1], [1]-3, -3) = 1, [1]
dp[3] = max(dp[2], 4, 4) = 4, [4]
dp[4] = max(dp[3], 4-1, -1) = 4, [4]
dp[5] = max(dp[4], 4-1+2, +2) = 5, [4,-1,2]
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        sub_end = nums[0]

        for i in range(1, len(nums)):
            if sub_end < 0: sub_end = 0
            sub_end += nums[i]
            dp.append(max([
                dp[i-1], sub_end, nums[i]
            ]))
        return dp[-1]
