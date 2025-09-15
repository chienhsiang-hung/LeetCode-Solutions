class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '#':
                    continue
                elif grid[r][c] == '0':
                    grid[r][c] = '#'
                    
                elif grid[r][c] == '1':
                    n += 1
                    self.dfs(grid, r, c)
        return n

    def dfs(self, grid, r, c):
        if (
            r == len(grid) or c == len(grid[0]) or
            r < 0 or c < 0
        ):
            return
        
        if grid[r][c] == '#':
            return
        elif grid[r][c] == '0':
            grid[r][c] = '#'

        elif grid[r][c] == '1':
            grid[r][c] = '#'
            self.dfs(grid, r, c+1)
            self.dfs(grid, r, c-1)
            self.dfs(grid, r+1, c)
            self.dfs(grid, r-1, c)

    

