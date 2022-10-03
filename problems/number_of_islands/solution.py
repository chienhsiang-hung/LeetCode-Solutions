class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_n = 0
        for r in range( len(grid) ):
            for c in range( len(grid[0]) ):
                if grid[r][c] == "1":
                    islands_n += 1
                    self.dfs(grid, r, c)
                else:
                    grid[r][c] = "checked"
        return islands_n
    
    def dfs(self, grid, r, c):
        if r<0 or c<0 or r>len(grid)-1 or c>len(grid[0])-1 or grid[r][c] in ["checked", "0"]:
            return
        
        grid[r][c] = "checked"

        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)