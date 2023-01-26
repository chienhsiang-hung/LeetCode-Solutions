class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_cnt = Counter()
        for n in nums:
            ele_cnt[n] += 1
            if ele_cnt[n] > len(nums)/2: return n