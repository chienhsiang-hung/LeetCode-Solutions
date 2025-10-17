'''
height = [1,8,6,2,5,4,8,3,7]
1: (1,7,8*1)
2: (8,7,7*2)
3: (8,7,7*3)
4: (8,7,7*4)
.
7: (8,7,7*7)
8: (8,8,8*5)
9: ()
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 1
        l = 0; r = len(height)-1
        
        ans = 0
        while l < r:
            while l < r and height[l] < i:
                l += 1
            
            while l < r and height[r] < i:
                r -= 1
            
            if max(height[r], height[l]) < i:
                break
            ans = max(ans, (r-l)*i)
            i += 1
        return ans
