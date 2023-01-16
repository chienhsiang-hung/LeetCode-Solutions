# [3,4,5,1,2]
# l=0 r=4, mid=2
# 5>3, l=3 r=4, mid=3
# 1<3, l=3 r=2...

# [3,1,2]
# l=0 r=2, mid=1
# ...

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        local_min = nums[0]
        while l <= r:
            mid = (l+r) // 2
            if nums[0] > nums[mid]:
                r = mid-1
                local_min = min(nums[mid], local_min)
            else:
                l = mid+1
        
        return local_min