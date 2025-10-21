'''
[1,1,1,1,2,2,2,3]
     l   r
     2 l   r
       2 l     r

[1,2,2,2,3,3,3,3]
     l
     r
       l r
       3 l r
       3,3 l r
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        l = r = 2
        while  r < len(nums):
            while nums[r] == nums[l-2]:
                r += 1
                if r == len(nums):
                    return l
            nums[l] = nums[r]
            l += 1
            r += 1
        return l
            
