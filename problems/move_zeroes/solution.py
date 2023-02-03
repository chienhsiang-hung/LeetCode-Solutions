class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # two pointer
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            while nums[r] == 0 or l == r:
                r += 1
                if r == len(nums): return
            
            if nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1