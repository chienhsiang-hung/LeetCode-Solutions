from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = defaultdict(list)
        for i, n in enumerate(nums):
            n_dict[n].append(i)

        for k, v in list(n_dict.items()):
            # [3,3], 6
            if k*2 == target and len(v) >= 2:
                return [v[0], v[1]]
            elif k*2 != target and n_dict[target-k]:
                return [v[0], n_dict[target-k][0]]
