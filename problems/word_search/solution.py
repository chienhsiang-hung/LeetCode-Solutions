from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check_word(r, c, i, word, visited):
            visited[(r,c)] = True
            for new_r, new_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0<=new_r<len(board) and 0<=new_c<len(board[0]):
                    if visited[(new_r,new_c)]:
                        continue
                    if board[new_r][new_c] == word[i]:
                        if i+1 < len(word):
                            check_word(new_r, new_c, i+1, word, visited.copy())
                        # reach the end
                        else:
                            finding.append(True)
                            return

        finding = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if 1 < len(word):
                        visited = defaultdict(lambda:False)
                        check_word(r, c, 1, word, visited.copy())
                        if any(finding):
                            return True
                    else:
                        return True

        return any(finding)
                    