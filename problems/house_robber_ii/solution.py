import functools

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        @cache
        def robber1_dp(n, _from=0):
            if _from == 0:
                if n == 0:
                    return nums[0]
                elif n == 1:
                    return max(nums[0], nums[1])
            else:
                if n == 1:
                    return nums[1]
                elif n == 2:
                    return max(nums[1], nums[2])
            
            v0, v1 = robber1_dp(n-2, _from), robber1_dp(n-1, _from)
            return max(v1, v0+nums[n])
        
        return max(
            robber1_dp(len(nums)-2),
            robber1_dp(len(nums)-1, 1)
        )