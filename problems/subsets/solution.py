# [1,2,3,4]
# n=0: [[]]
# n=1: [[1]] + n=0
# n=2: [[2]] + [[1,2]] + n=1
# n=3: [[3]] + [[3,1], [3,2]] + [[1,2,3]] + n=2

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dp(n):
            if n == 0:
                return [[]]
            
            last_layer = dp(n-1)
            output = []
            for item in last_layer:
                output.append(
                    item + [nums[n-1]]
                )
            return output + last_layer
        
        return dp(len(nums))
            