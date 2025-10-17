'''
[-1, 1,0,-3,3]
[-1,-1,0, 0,0] fromL
[ 0, 0,0,-9,3] fromR
[ 0, 0,9, 0,0]
'''
from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromL = [nums[0]]
        for i in range(1, len(nums)):
            fromL.append(fromL[-1]*nums[i])
        
        fromR = deque([nums[-1]])
        for i in range(len(nums)-2, -1, -1):
            fromR.appendleft(fromR[0]*nums[i])
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(fromR[1])
            elif i == len(nums)-1:
                res.append(fromL[-2])
            else:
                res.append(fromL[i-1]*fromR[i+1])
        return res
