from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # O(n)
        
        bucket = [
            [] for _ in range(len(nums)+1)
        ]
        for key, v in freq.items():
            bucket[v].append(key)
        
        res = []
        i = len(bucket)-1
        while len(res) < k:
            if bucket[i]:
                res.append(bucket[i].pop())
            else:
                i -= 1
        return res
            
