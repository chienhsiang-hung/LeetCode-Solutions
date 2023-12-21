class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = dict()
        for n in nums:
            if n in store: return True
            store[n] = True
        
        return False