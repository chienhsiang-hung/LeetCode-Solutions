'''
[25,49,75], 13, 1

'''
from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        # target not in arr
        l = 0
        ans = 1
        opeLeft = numOperations-1
        for i in range(1, len(nums)):
            opeLeft -= 1
            while nums[l] + min(numOperations, 2)*k < nums[i] or opeLeft < 0:
                l += 1
                opeLeft = min(numOperations, opeLeft+1)
                if l == i: break
            ans = max(ans, i-l+1)

        # target in arr
        ctn = Counter(nums)
        ctn_v = sorted(ctn.keys())
        for i, v in enumerate(ctn_v):
            left = bisect_left(nums, v-k)
            right = bisect_right(nums, v+k)
            length = right - left
            ans = max(
                ans,
                ctn[v] + min(numOperations, length-ctn[v])
            )
            
        return ans
                
