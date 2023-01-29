class Solution:
    def distinctIntegers(self, n: int) -> int:
        board = set()
        board_q = deque([n])
        while board_q:
            curr = board_q.popleft()
            
            if curr in board:
                continue
            board.add(curr)
                
            for i in range(curr-1, 0, -1):
                if curr%i == 1:
                    board_q.append(i)
        
        return len(board)
                
        