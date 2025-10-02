from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        [-1,0,0,3,0,-1,-4], k=2
        -1
        -1, 0
        -1, 0, 0
        -1, 0, 0, 3
        -1, 0, 0, 3, 0
        0, 0, 3, 0, -1
        .
        .
        .
        too complex
        '''
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        n_valid = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            n_valid += prefix_map[curr-k]

            prefix_map[curr] += 1
        return n_valid

