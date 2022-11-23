# [5,3,1]
# f(0) = num[0] = 5
# f(1) = max(num[0], num[1]) = 5
# f(2) = max(f(0)+num[2], f(1)) = max(5+1, 5) 

# [1,3,1]
# f(0) = num[0] = 1
# f(1) = max(num[0], num[1]) = 3
# f(2) = max(f(0)+num[2], f(1)) = max(1+1, 3)

# [5,3,1,100]
# f(0) = num[0] = 5
# f(1) = max(num[0], num[1]) = 5
# f(2) = max(f(0)+num[2], f(1)) = max(5+1, 5) = 6
# f(3) = max(f(1)+num[3], f(2)) = max(5+100, 6) = 105
# ...
# f(i) = max(f(i-2)+num[i], f(i-1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = nums[0]
        if len(nums) == 1:
            return f0
        f1 = max(nums[0], nums[1])
        for n in nums[2:]:
            new = max(f0+n, f1)
            f0 = f1
            f1 = new
        return f1