from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_bank = defaultdict(lambda: False)
        for i, n in enumerate(nums):
            # output = [x,x]
            if n*2 == target:
                for j in range(len(nums[i+1:])):
                    if nums[i+j+1] == n:
                        return[i, i+j+1]
            # output = [x,y]
            if n_bank[n]!=False and type(n_bank[target-n])!=bool:
                return [n_bank[target-n], i]
            n_bank[n] = i
            n_bank[target-n] = True