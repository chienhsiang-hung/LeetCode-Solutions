# with the constraints num[i] is int, we know the number itself will only grow larger

# Cases:
#
# 2, 3, -2, 4
# [2, 6, -12, -48] + [-48, -24, -8, 4] find the max inside
# the largest will either lie in the right side or left side
#
# new_list[i] = num[i]*(num[i-1] or 1)
# 3, -5, 0, 100, 0, 10, 1
# [3, -15, 0, 100, 0] + [3, -5, 0, 100, 0, 10, 1]
# and find the largest it is then

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reversed = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            nums_reversed[i] *= nums_reversed[i-1] or 1
        return max(nums+nums_reversed)