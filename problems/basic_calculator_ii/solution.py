# brute force - iterate first time to rec the numbs and operations
# then find the operations to to the calculation
# finallly sum them up

from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        # build nums_list
        l = r = 0
        nums = deque()
        while r < len(s):
            if s[r] in ['+', '-', '*', '/']:
                nums.append(int(s[l:r]))
                nums.append(s[r])
                l = r+1
            r += 1
        nums.append(int(s[l:r]))

        add = []
        # calculate * and /
        while nums:
            current = nums.popleft()
            if current == '*':
                add[-1] = int(add[-1] * nums.popleft())
            elif current == '/':
                add[-1] = int(add[-1] / nums.popleft())
            elif current == '+':
                add.append(nums.popleft())
            elif current == '-':
                add.append(-nums.popleft())
            
            else:
                add.append(current)
        
        return sum(add)
             
        