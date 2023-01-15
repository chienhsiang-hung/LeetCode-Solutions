class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = 0
        dig_sum = 0
        for n in nums:
            ele_sum += n
            for j in str(n):
                dig_sum += int(j)
        
        return abs(ele_sum-dig_sum)