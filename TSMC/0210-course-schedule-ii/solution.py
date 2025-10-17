'''
[[1,0],[2,0],[3,1],[3,2]]
0: N
1: 0
2: 0
3: 1,2

1>0>N [0,1]
0: N
1: N
2: 0
3: 1,2

2>0>N [0,1,2]
0: N
1: N
2: N
3: 1,2

[[1,0]]
'''
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        csMap = defaultdict(set)
        for c, p in prerequisites:
            csMap[c].add(p)
        
        def dfs(c):
            if c in vis:
                return False
            vis.add(c)

            if csMap[c]:
                for p in set(csMap[c]):
                    
                    if not dfs(p): return False
                    csMap[c].remove(p)
                    vis.remove(p)
                if c not in taken:
                    taken.add(c)
                    res.append(c)
                return True

            if c not in taken:
                taken.add(c)
                res.append(c)
            return True
        
        res = []
        taken = set()
        for c in range(numCourses):
            vis = set()
            if not dfs(c): return []
        return res if len(res) == numCourses else []
