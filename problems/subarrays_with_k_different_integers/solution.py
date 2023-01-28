# https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/523136/java-c-python-sliding-window/
# https://www.youtube.com/watch?v=eBKv6-m4NDQ

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return (
            self.subarraysWithAtMostDistinct(nums, k) -
            self.subarraysWithAtMostDistinct(nums, k-1)
        )
    
    def subarraysWithAtMostDistinct(self, nums, k):
        n_ct = Counter()
        l = subs = 0
        for i in range(len(nums)):
            if n_ct[nums[i]] == 0: k -= 1
            n_ct[nums[i]] += 1
            
            while k < 0:
                n_ct[nums[l]] -= 1
                if n_ct[nums[l]] == 0: k += 1
                l += 1
                
            subs += i-l +1
            # for [1,2,1,2], [3]
            # i-l means [2], +1 means [3]
        return subs 