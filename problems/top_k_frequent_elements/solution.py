class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctn = Counter(nums)
        std_arr = sorted(
            [(k, ctn[k]) for k in ctn.keys()],
            key = lambda tpl: tpl[1],
            reverse = True
        )
        return [k for k, _ in std_arr[:k]]