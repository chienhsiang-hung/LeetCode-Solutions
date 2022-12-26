# DFS
# Check route from the border and DFS into the center. Seperate check for Atlantic and Pacific.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        atlantic = set()
        pacific = set()
        
        def traverse(r, c, check_set):
            if (r, c) in check_set:
                return
            check_set.add((r, c)) 
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r+dr
                new_c = c+dc
                # check if new_r and new_c are valid
                if 0<=new_r<len(heights) and 0<=new_c<len(heights[0]):
                    # if it's sourcible
                    if heights[new_r][new_c]>=heights[r][c]:
                        traverse(new_r, new_c, check_set)
        
        # border traverse
        for r in range(len(heights)):
            traverse(r, 0, pacific) # left
            traverse(r, len(heights[0])-1, atlantic) # right
        for c in range(len(heights[0])):
            traverse(0, c, pacific) # top
            traverse(len(heights)-1, c, atlantic) # bottom
        
        return list(pacific & atlantic)
            
