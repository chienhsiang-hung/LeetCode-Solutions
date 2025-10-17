'''
[2,7,9,3,1]
f(0) = 2
f(1) = 7
f(2) = max(9+f(0), f(1))
f(3) = max(...)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) == 1: return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]
            
