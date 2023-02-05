# [100,4,200,1,3,2]
# 100, 101 not in 
# 4, 5 not in
# 200, 201 not in
# 1, 2 in
# 2, 3 in
# 3, 4 in

# need a help of visited

# [100,2,3,4,200,5,3,2,1]
# [5,4,5,3,4,5,2,3,4,5]
# [5,4,3,2,1]
# [1,2,5,6]
# [100,99,98]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = set(nums)
        best = 0
        for n in nums:
            pre = curr = n
            local_streak = 1
            if curr-1 not in nums_map:
                while curr+1 in nums_map:
                    local_streak += 1
                    curr += 1
                best = max(best, local_streak)
        return best
                    
        
            