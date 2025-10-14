class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.end = True
    
    def find(self, word):
        cur = self.root

        word_list = []
        for c in word:
            if c not in cur.child:
                return []
            word_list.append(c)
            cur = cur.child[c]
        return [''.join(word_list)] if cur.end else []

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add(word)

        def dfs(curNode, i, j, word=[]):
            word.append(board[i][j])
            if word[-1] not in curNode.child:
                word.pop()
                return

            if curNode.child[word[-1]].end:
                found.append(''.join(word))
                curNode.child[word[-1]].end = False
            if not curNode.child[word[-1]].end and not curNode.child[word[-1]].child:
                curNode.child.pop(word[-1], None)
            
            for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                if (
                    0<=i+dr<len(board) and
                    0<=j+dc<len(board[0]) and
                    (i+dr, j+dc) not in vis and
                    word[-1] in curNode.child
                ):
                    vis.add((i+dr, j+dc))
                    dfs(curNode.child[word[-1]], i+dr, j+dc, word)
                    vis.remove((i+dr, j+dc))
            word.pop()

        ans = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                vis = {(r, c)}
                found = []
                dfs(trie.root, r, c)
                for found_w in found:
                    ans.add(found_w)
        return list(ans)

