from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(bool)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        for _chr in key:
            if current.children[_chr]:
                current = current.children[_chr]
            else:
                current.children[_chr] = TrieNode()
                current = current.children[_chr]
        current.isEnd = True

    def search(self, key):
        current = self.root
        for _chr in key:
            if current.children[_chr]:
                current = current.children[_chr]
            else:
                return False
        return current.isEnd

    def word_in_trie(self, key):
        current = self.root
        for _chr in key:
            current = current.children[_chr]
            if not current:
                return False
        return True
    
    def list_words(self):
        current = self.root
        
        def dfs(current, word_snake):
            if not current: return
            
            for k, v in current.items():
                if v:
                    if current[k].isEnd:
                        output.append(
                            ''.join(word_snake+[k])
                        )
                    if current[k].children:
                        dfs(current[k].children, word_snake+[k])        
        
        output = []
        dfs(current.children, [])
        
        return output
    
    def remove(self, key):

        def recursive_down(current, i, key):
            if i == len(key):
                if all(v==False for v in current.children.values()):
                    return False
                else:
                    return current

            current.children[key[i]] = recursive_down(
                current.children[key[i]], i+1, key
            )
            return current

        current = self.root
        current.children[key[0]] = recursive_down(
            current.children[key[0]], 1, key
        )
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(r, c, word_snake=[], visited=defaultdict(), current=TrieNode().children):
            if visited[(r,c)]:
                return
            visited[(r,c)] = True
            
            word_snake.append(board[r][c])
            current_word = ''.join(word_snake)

            if current[board[r][c]]:
                if current[board[r][c]].isEnd:
                    output.add(current_word)
                    trie.remove(current_word)

            # if trie.word_in_trie(current_word):
            #     if trie.search(current_word):
            #         output.add(current_word)

                for new_r, new_c in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0<=new_r<len(board) and 0<=new_c<len(board[0]) and current[board[r][c]]:
                        dfs(new_r, new_c, [current_word], visited.copy(), current[board[r][c]].children)

        output = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                current = trie.root
                dfs(r, c, [], defaultdict(bool), current.children)
        
        return output