'''
[3,5,0,1,2,4]
[4]
[4,2]
[4,2,1]
[4,2,1,0]

[3,5,1,3,4,1]
5: [1]
4: k=1, [4]
3: k=1, [4,3]
3: k=1, [4,3,1]
2: k=4, [5]
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = float('-inf')

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < k:
                return True
            while stack and nums[i] > stack[-1]:
                k = stack.pop()
            stack.append(nums[i])
        return False
        

