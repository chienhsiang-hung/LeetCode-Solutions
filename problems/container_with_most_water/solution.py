# the area = min(left, right) * width
# [1,8,6,2,5,4,8,3,9,7]
# (0,1), (1,8) -> 1*1=1
# next
# [
#     ((0,1), (1,8)) -> 1
#     ((1,8), (2,6)) -> 6
#     ((0,1), (2,6)) -> 2
# ]

# brute force will be O(n*n)
# how to optmize it to O(n)
# [1,8,6,2,5,4,8,3,9,7]
# (1,0)->(7,9)->1*9=9
# mv the short one because you will never need to use it as you shorten the distance
# (8,1)->(7,9)->7*8=56

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        container = 0
        while l < r:
            container = max(
                container,
                min(height[l], height[r]) * (r-l)
            )
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        
        return container
                

                