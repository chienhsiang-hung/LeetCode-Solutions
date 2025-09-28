from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                # BFS

                visited = set()
                q = deque([(r, c)])
                pac = atl = False
                while q:
                    cell = q.popleft()
                    if cell in visited:
                        continue
                    visited.add(cell)
                    
                    # condition check
                    if cell[0]==0 or cell[1]==0:
                        pac=True
                    if cell[0]==len(heights)-1 or cell[1]==len(heights[0])-1:
                        atl=True
                    
                    # path check
                    up = (cell[0]-1, cell[1])
                    down = (cell[0]+1, cell[1])
                    right = (cell[0], cell[1]+1)
                    left = (cell[0], cell[1]-1)
                    for nr, nc in [up, down, right, left]:
                        # check valid and go-able
                        if (
                            0 <= nr < len(heights) and 0 <= nc < len(heights[0])
                        ) and heights[nr][nc] <= heights[cell[0]][cell[1]]:
                            q.append((nr, nc))
                if pac and atl: res.append([r, c])
        return res
