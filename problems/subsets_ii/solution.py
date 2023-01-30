# [1,2,2,2]
# 0, [[]]
# 1, [[1]]
# 2, [[2],[1,2]]
# 2, [[2],[1,2],[2,2],[1,2,2]] -> [[2,2],[1,2,2]] -2
# 2, [[2],[1,2],[2,2],[1,2,2],[2,2],[1,2,2],[2,2,2],[1,2,2,2]] ->  -4

# [1,1]
# 0, [[]]
# 1, [[1]]
# 1, [[1],[1,1]]

# [1,1,2,2]
# 0, [[]]
# 1, [[1]]
# 1, [[1],[1,1]] -> [[1,1]]
# 2, [[2],[1,2],[1,1,2]]
# 2, [[2,2],[1,2,2],[1,1,2,2]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        def dp(n):
            if n == 0:
                output.append([])
                return [[]]

            last_layer = dp(n-1)
            current = []
            if nums[n-1] == nums[n-2]:
                for item in last_layer:
                    current.append(item + [nums[n-1]])
                    output.append(item + [nums[n-1]])
                return current
            for item in output:
                current.append(item + [nums[n-1]])
            output.extend(current)
            return current
        dp(len(nums))
        return output