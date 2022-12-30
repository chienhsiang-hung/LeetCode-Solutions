# brute force

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def add_num(_list, _rest):
            if not _rest:
                output.append(_list)
                return

            for i in range(len(_rest)):
                add_num(
                    _list + [_rest[i]],
                    _rest[:i] + _rest[i+1:]
                )

        output = []
        for i in range(len(nums)):
            add_num(
                [nums[i]],
                nums[:i] + nums[i+1:]
            )
        
        return output