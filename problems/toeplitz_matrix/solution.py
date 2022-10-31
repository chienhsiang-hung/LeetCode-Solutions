class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        r, c = height-1, 0
        while r < height and c < width:
            current = matrix[r][c]
            outer_r, outer_c = r, c
            r += 1
            c += 1
            while r < height and c < width:
                if matrix[r][c] != current:
                    return False
                r += 1
                c += 1
            c = outer_c+1 if outer_r==0 else 0
            r = outer_r-1 if outer_r-1>=0 else 0
        return True
                    