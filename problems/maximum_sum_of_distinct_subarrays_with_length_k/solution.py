from collections import defaultdict, deque

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        
        window_dict = defaultdict(int)
        one_chr = set()
        
        max_sum = 0
        local_sum = 0
        for i in range(len(nums)):
           # widow right
            local_sum += nums[i]
            window_dict[nums[i]] += 1
            one_chr.add(nums[i])
            # the right part needs to be placed before the left part

            # windoe left
            if i >= k:
                local_sum -= nums[i-k]
                window_dict[nums[i-k]] -= 1
                if window_dict[nums[i-k]] == 0:
                    if nums[i-k] in one_chr:
                        one_chr.remove(nums[i-k])
 
            if len(one_chr) == k:
                if local_sum > max_sum:
                    max_sum = local_sum
        return max_sum