class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # -> v
        # v <-
        # <- ^
        # ^ ->
        ans = []
        self.right(matrix, 0, 0, ans)
        
        return ans

    def right(self, matrix, r, c, ans):
        if c == len(matrix[0]) or matrix[r][c] == '#':
            return

        for i in range(c, len(matrix[0])):
            if matrix[r][i] == '#':
                self.down(matrix, r+1, i-1, ans)
                return
            ans.append(matrix[r][i])
            matrix[r][i] = '#'
        self.down(matrix, r+1, i, ans)

    def down(self, matrix, r, c, ans):
        if r == len(matrix) or matrix[r][c] == '#':
            return

        for i in range(r, len(matrix)):
            if matrix[i][c] == '#':
                self.left(matrix, i-1, c-1, ans)
                return
            ans.append(matrix[i][c])
            matrix[i][c] = '#'
        self.left(matrix, i, c-1, ans)

    def left(self, matrix, r, c, ans):
        if c < 0 or matrix[r][c] == '#':
            return

        for i in range(c, -1, -1):
            if matrix[r][i] == '#':
                self.up(matrix, r-1, i+1, ans)
                return
            ans.append(matrix[r][i])
            matrix[r][i] = '#'
        self.up(matrix, r-1, i, ans)

    def up(self, matrix, r, c, ans):
        if matrix[r][c] == '#':
            return

        for i in range(r, -1, -1):
            if matrix[i][c] == '#':
                self.right(matrix, i+1, c+1, ans)
                return
            ans.append(matrix[i][c])
            matrix[i][c] = '#'
