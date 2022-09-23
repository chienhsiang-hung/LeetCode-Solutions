class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            _sum -= n
            if left_sum == _sum:
                return i
            left_sum += n
        return -1

            