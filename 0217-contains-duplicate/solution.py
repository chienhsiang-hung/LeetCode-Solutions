from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        for k, v in ctr.items():
            if v >= 2:
                return True
        return False
