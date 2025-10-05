'''
[2,3,-2, 1,-4,0,5,-1,100]
 2 6 -12-2 8  0 0 -5  0 
M2 6 -2 -2 48 0 5  0 100
 2 6 -6 -1248 0 0  0-500
m2 3 -12-12-4 0 0 -5-500

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1, len(nums)):
            tmp_max = nums[i] * curr_max
            curr_max = max([
                nums[i], curr_max*nums[i], curr_min*nums[i]
            ])
            curr_min = min([
                nums[i], tmp_max, curr_min*nums[i]
            ])
            ans = max(ans, curr_max)

        return ans
