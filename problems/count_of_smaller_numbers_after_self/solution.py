# Concept

# [5,2,1,5,2,2,6,1]
# [7,6,5,4,3,2,1,0]

# divide:
# [5,2,1,5,2][2,6,1]
# [5,2,1][5,2][2][6,1]
# [5][2,1] [5][2] [2] [6][1]

# conquer:
# [(5,0)] [(2,1),(1,2)] [(5,3),(2,4)] [(2,5)] [(6,6)][(1,7)]
# [(5,0),(2,1),(1,2)] [(5,3),(2,4)] [(2,5)] [(6,6),(1,7)]
# [6,4,3,4,3,1,1,0] -2, -1
# [(5,3)(5,0)(2,4)(2,1)(1,2)] [(6,6)(2,5)(1,7)]
# [5,2,0,3,1,1,1,0] -3
# [(6,6)(5,3)(5,0)(2,5)(2,4)(2,1)(1,7)(1,2)]

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/solutions/76584/mergesort-solution/
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/solutions/445769/merge-sort-clear-simple-explanation-with-examples-o-n-lg-n/


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [(n, i) for i, n in enumerate(nums)]
        r_eles_to_index = list( range(len(nums)) )[::-1]
        
        def divide_and_conquer(nums):
            if len(nums) <= 1: return nums
            mid = len(nums) // 2
            left = divide_and_conquer(nums[:mid])
            right = divide_and_conquer(nums[mid:])

            l = r = 0
            subtr = 0
            merged = []
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    merged.append(left[l])
                    r_eles_to_index[left[l][1]] -= subtr
                    l += 1
                else:
                    subtr += 1
                    merged.append(right[r])
                    r += 1
            
            while l < len(left):
                merged.append(left[l])
                r_eles_to_index[left[l][1]] -= subtr
                l += 1
            
            while r < len(right):
                merged.append(right[r])
                r += 1
            
            return merged
        
        divide_and_conquer(nums)
        return r_eles_to_index

            
                    


            
            
