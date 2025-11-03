'''
[3,2,1,0,4]
i3: >=1, fail
i2: >=1+1, fail
i1: >=2+1, fail
i0: >=3+1, fail

[3,4,2,1,0,4]
i4: >=1, fail
i3: >=1+1, fail
i2: >=2+1, fail
i1: >=3+1, success
i0: >=1, success
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        req_stp = 1
        ans = True
        for i in range(len(nums)-1-1, -1, -1):
            if nums[i] >= req_stp:
                req_stp = 1
                ans = True
            else:
                req_stp += 1
                ans = False
        return ans
