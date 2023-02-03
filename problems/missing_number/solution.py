# 0,1=> 1
# 0,1,2=> 3
# 0,1,2,3=> 6=3*(len/2)
# 0,1,2,3,4=> 10=4*(len/2)
# 0,1,2,3,4,5=> 15=5*(len/2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(
            len(nums) * ( len(nums)+1 )/2 - sum(nums)
        )