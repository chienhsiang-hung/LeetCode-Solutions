class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        # remove unqualified candidate
        while candidates and candidates[-1] > target:
            candidates.pop()

        def loop(_list, _sum, _idx, target):
            '''
            @curr_list
            @curr_sum
            @curr_idx
            '''
            if _sum > target:
                return
            elif _sum == target:
                output.append(_list)
                return

            for i in range(_idx, len(candidates)):
                loop(
                    _list + [candidates[i]],
                    _sum + candidates[i],
                    i,
                    target
                )
        
        output = []
        loop([], 0, 0, target)
        
        return output