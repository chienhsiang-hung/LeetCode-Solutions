class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l <= r:
            m = (l+r) // 2

            if target == nums[m]:
                return m

            # turn right
            if ( 
                target < nums[m] and 
                nums[m] >= nums[l] > target
            ):
                l = m + 1
                continue
            
            # turn left
            if (
                target > nums[m] and 
                target > nums[r] >= nums[m]
            ):
                r = m - 1
                continue
        
            # turn right
            if (target > nums[m]):
                l = m + 1
                continue
            # turn left
            if target < nums[m]:
                r = m - 1
                continue
        return -1
