class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _sum = 0
        for i, n in enumerate(nums):
            _sum += n
            nums[i] = _sum
        return nums
            