from collections import deque

class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        '''
        '.b.' BFS
        '''
        q = deque([
            (self.root, 0)
        ])
        
        ans = False

        while q:
            cur, i = q.popleft()

            if i == len(word): continue

            if word[i] != '.':
                if word[i] not in cur.child:
                    continue

                if i == len(word) -1 and cur.child[word[i]].endOfWord:
                    ans = True
                    return ans
                
                q.append(
                    (cur.child[word[i]], i+1)
                )
            else: # when it's '.'
                for child in cur.child:
                    if i == len(word)-1 and cur.child[child].endOfWord:
                        ans = True
                        return ans
                    q.append((cur.child[child], i+1))
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
