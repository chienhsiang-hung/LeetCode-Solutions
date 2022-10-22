# Two situations:
#   1. nums = [4,5,6,7,0,1,2], target = 0
#   2. nums = [4,5,6,7,0,1,2], target = 5
#
# In the first situation, target < nums[0]. If the 'current' num is bigger than the nums[0], we go right...
# vise versa

# Edge cases:
# [3,1], t=1
# mid=(0+1)//2=0, current=3
# mid=(1+1)//2=1...#
#
# [1,3], t=3
# mid=0, current=1
#
# [1,3,5], t=1
# mid=(0+2)//2=1, current=3
#
# [3,5,1], t=3
# mid=1, current=5
#
# [4,5,6,7,0,1,2], t=0
# mid=(0+6)//2=3, current=7
# mid=(4+6)//2=5, current=1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right) // 2
            current = nums[mid]
            if current == target:
                return mid

            # [6,7,1,2,3,4,5], t=7
            if current <= nums[-1] < target and current < target:
                right = mid-1
            # [3,4,5,6,7,1,2], t=2
            elif current >= nums[0] > target and current > target:
                left = mid+1
            
            else:
                if current < target:
                    left = mid+1
                else:
                    right = mid-1
        return -1
            