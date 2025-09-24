class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, path = [], []

        def dfs(start, remain):
            if remain == 0:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                
                if candidates[i] > remain: return
                
                path.append(candidates[i])
                dfs(i, remain-candidates[i])
                path.pop()
        
        dfs(0, target)
        return ans
