'''
[0,1,0,2,1,0,1,3,2,1,2,1]
[0,1,1,2,2,2,2,3,3,3,3,3] toRight
[3,3,3,3,3,3,3,3,2,2,2,1] toLeft
[0,0,1,0,1,2,1,0,0,1,0,0]
'''
from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0

        toRight = [height[0]]
        for i in range(1, len(height)):
            toRight.append(max(toRight[-1], height[i]))

        toLeft = deque([height[-1]])
        for i in range(len(height)-1, -1, -1):
            toLeft.appendleft(max(height[i], toLeft[0]))
        
        ans = 0
        for i in range(1, len(height)-1):
            ans += max(0, min(toRight[i-1], toLeft[i+1]) - height[i])

        return ans
        
