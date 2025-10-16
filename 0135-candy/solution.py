'''
[1,0,2]
[2,1,2]

[1,2,2]
[1,2,1]

[3,4,8,7,6,0,2,2,1]
 1,2,4,3,2,1,2,2,1

[3,4,8,7,6,0,2,2,1]
[1,2,3,1,1,1,2,1,1]
[1,1,4,3,2,1,1,2,1]

[1,2,2]
[1,2,1]
[1,1,1]
'''
from collections import deque
class Solution:
    def candy(self, ratings: List[int]) -> int:
        toRight = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                toRight.append(toRight[-1]+1)
            else:
                toRight.append(1)

        toLeft = deque([1])
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                toLeft.appendleft(toLeft[0]+1)
            else:
                toLeft.appendleft(1)
        
        ans = 0
        for i in range(len(ratings)):
            ans += max(toLeft[i], toRight[i])
        return ans
