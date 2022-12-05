# modified the number not chang it's position
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        i = 3
        changed_needed = 0

        while i<=len(nums) and changed_needed<=1:
            window = nums[i-3:i]

            if window[0] > window[1] > window[2]:
                return False
                
            # 3,4,2,3 / 1,2,3,5,6,7,4
            elif window[0] > window[2] and window[1] > window[2]:
                changed_needed += 1
                nums[i-1] = nums[i-2]
            elif window[0] > window[1] <= window[2]:
                changed_needed += 1
                nums[i-3] = nums[i-2]
            # -1,4,2,3
            elif window[0] <= window[1] > window[2]:
                changed_needed += 1
                nums[i-2] = nums[i-1]

            i += 1
        
        return changed_needed <= 1