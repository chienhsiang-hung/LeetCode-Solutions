# optimized BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # track all 0 first
        nodes = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    nodes.append((r, c, 0))

        # [
        #     [0,0,0],
        #     [0,1,0],
        #     [1,1,1],
        #     [1,1,1]
        # ]

        visited = [
            [False] * len(mat[0]) for _ in range(len(mat))
        ]
        # BFS
        while nodes:
            r, c, dis = nodes.popleft() # with original mat value

            if visited[r][c]: continue
            visited[r][c] = True

            # update value
            mat[r][c] = dis

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                # node exists
                if 0<=r+dr<len(mat) and 0<=c+dc<len(mat[0]):
                    nodes.append((r+dr, c+dc, dis+1))
        
        return mat