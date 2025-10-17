'''
[1,2,3,1,4,6,1]
f(0) = 1
f(1) = 2
f(2) = 3
f(3) = 4 # 1+3 [1,2,3], [2,3,1]
f(4) = 7 # 3+4 [1,2,3,1], [2,3,1,4]
f(5) = 9 # [1,2,3,1,4], [2,3,1,4,6]
f(6) = 10 # [1,2,3,1,4,6], [2,3,1,4,6,1]

[4,3,2,1]
f(0) = 4
f(1) = 4
f(3) = 4
f(4) = 6 # 4+2 [4,3,2], [2,3,1]

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * (len(nums)-1)
        dp2 = [0] * (len(nums)-1)

        if len(nums) <= 3: return max(nums)

        dp1[0] = nums[0]
        dp1[1] = max(nums[:2])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1:3])

        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2]+nums[i+1], dp2[i-1])
        
        return max(dp1[-1], dp2[-1])
