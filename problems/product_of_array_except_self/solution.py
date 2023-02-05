# [1,2,3,4]
# [1,1,1,1]     1,4
# [1,1,4,1]     2,12
# [1,12,8,1]    6,24
# [24,12,8,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = suf = 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1-i] *= suf
            suf *= nums[-1-i]
        return ans