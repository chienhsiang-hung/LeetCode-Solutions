class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = global_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum+nums[i], nums[i])
            global_sum = max(current_sum, global_sum)
        
        return global_sum