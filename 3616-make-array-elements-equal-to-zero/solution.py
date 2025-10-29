class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def traverse(i, _dir):
            while 0 <= i < len(nums_copy):
                if nums_copy[i] == 0:
                    i += _dir
                    continue
                
                if nums_copy[i] > 0:
                    nums_copy[i] -= 1
                    _dir *= -1
                    i += _dir
            return all(n == 0 for n in nums_copy)
        
        ans = 0
        for i, n in enumerate(nums):
            if n != 0:
                continue
            
            for j in (1, -1):
                nums_copy = [n for n in nums]
                if traverse(i, j): ans += 1
        return ans
