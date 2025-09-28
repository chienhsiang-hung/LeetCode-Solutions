class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word)>len(board)*len(board[0]): return False
        # Let's practice DFS this time

        def dfs(i, j, word=word, k=0):
            if board[i][j] != word[k] or visited[i][j]:
                return False
            if board[i][j] == word[k] and k == len(word)-1:
                return True
            
            visited[i][j] = True
            for v, h in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if 0<=i+v<len(board) and 0<=j+h<len(board[0]):
                    if dfs(i+v, j+h, k=k+1): return True
            
            visited[i][j] = False
            return False
                        
        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = [
                    [False]*len(board[0]) for _ in range(len(board))
                ]
                if dfs(r, c): return True
        
        return False
