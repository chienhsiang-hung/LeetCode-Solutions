# sort the array
# [-4, -1, 1, 2], 1
# [-70, -10, 50, 60, 70], 50


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[-1]
        diff = abs(closest - target)
        for i in range(len(nums)-2):
            left = i
            mid = left +1
            right = len(nums) -1

            while mid < right:
                local_closest = nums[left] + nums[mid] + nums[right]
                local_diff = abs(local_closest - target)
                
                if local_diff == 0: return local_closest
                if local_diff < diff:
                    diff = local_diff
                    closest = local_closest
                    
                if local_closest > target:
                    right -= 1
                else:
                    mid += 1
        return closest

            