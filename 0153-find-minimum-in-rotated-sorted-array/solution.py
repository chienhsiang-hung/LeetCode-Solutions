'''
[4,5,6,7,0,1,2]
 L     M     R
         L M R
         M R
         L
         R
[2,4,5,6,7,0,1]
 L     M     R
         L M R
         L R
         M L
           R
           M
[3,4,5,1,2]
 L   M   R
       L R
       M
       L
       R
       M
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r) //2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]
