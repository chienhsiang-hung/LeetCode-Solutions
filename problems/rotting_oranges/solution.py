class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # record rotten and fresh oranges
        rottens = []
        freshs = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshs.append((r,c))
                elif grid[r][c] == 2:
                    rottens.append((r,c))
        
        # check the edge cases
        # (1)(2)()
        if freshs and not rottens:
            return -1
        elif rottens and not freshs:
            return 0
        elif not rottens and not freshs:
            return 0
        
        total_orange = len(rottens) + len(freshs)
        mom = 0
        # rotting oranges
        new_rottens = []
        total_rottens = rottens.copy()
        while len(total_rottens) != total_orange:
            mom += 1
            # BFS
            for r, c in rottens:
                # up
                if r-1>=0:
                    if grid[r-1][c] == 1:
                        grid[r-1][c] = 2
                        new_rottens.append((r-1,c))
                # right
                if c+1<=len(grid[0])-1:
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        new_rottens.append((r,c+1))
                # down
                if r+1<=len(grid)-1:
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        new_rottens.append((r+1,c))
                # left
                if c-1>=0:
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        new_rottens.append((r,c-1))
                        
            # check if there is no change in this round, means it's not possible
            if not new_rottens:
                return -1
                
            total_rottens += new_rottens
            rottens = new_rottens.copy()
            new_rottens = []

        return mom            
            
                