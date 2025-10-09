from collections import deque
'''
2,1,1
1,1,1
0,1,2
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orgs = deque()
        fresh = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh = True
                elif grid[r][c] == 2:
                    orgs.append((r,c,0))
        if not orgs:
            if not fresh: return 0
            return -1
        
        while orgs:
            r, c, state = orgs.popleft()
            final_state = state
            for dr, dc in ((0,1), (1,0), (-1,0), (0,-1)):
                if (
                    0<=r+dr<=len(grid)-1 and 0<=c+dc<=len(grid[0])-1 and
                    grid[r+dr][c+dc] not in [0,2]
                ):
                    grid[r+dr][c+dc] = 2
                    orgs.append((r+dr, c+dc, state+1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return final_state
