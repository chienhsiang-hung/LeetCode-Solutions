# brute force
# double loop through the array and check lcm

# calculate GCD for LCM
# x, y = y, x%y
# 300, 400
# 400, 300
# 300, 100
# 100, 0

# 100, 29
# 29, 13
# 13, 3
# 3, 1
# 1, 0

# https://www.programiz.com/python-programming/examples/lcm
# https://www.programiz.com/python-programming/examples/hcf
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        def lcm(x, y):
            xy = abs(x*y)
            while y:
                x, y = y, x%y
            # LCM = |x*y| / GCD(x,y)
            return xy / x

        n_k = 0
        for i in range(len(nums)):
            current_lcm = nums[i]
            for j in range(i, len(nums)):
                current_lcm = lcm(current_lcm, nums[j])
                if current_lcm == k:
                    n_k += 1
                if current_lcm > k:
                    break
        return n_k