class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def bfs(left, mid, right, rows=[], n=n):
            if len(rows) == n:
                solutions.append(rows)
                return
            for c in range(n):
                if left[c]==0 and mid[c]==0 and right[c]==0:
                    this_row = ['.']*n
                    this_row[c] = 'Q'

                    # update occupied
                    new_left = left[1:] + [0]
                    if c-1 >= 0:
                        new_left[c-1] = 1
                    new_mid = mid[:c] + [1] + mid[c+1:]
                    new_right = [0] + right[:-1]
                    if c+1 < n:
                        new_right[c+1] = 1
                    
                    bfs(new_left, new_mid, new_right, rows+[''.join(this_row)])
        solutions = []
        bfs([0]*n, [0]*n, [0]*n)
        return solutions