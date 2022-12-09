from collections import defaultdict


class TrieNode:

    def __init__(self) -> None:
        self.children = defaultdict(bool)
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if current.children[ch]:
                current = current.children[ch]
            else:
                current.children[ch] = TrieNode()
                current = current.children[ch]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            if current.children[ch]:
                current = current.children[ch]
            else:
                return False
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            if current.children[ch]:
                current = current.children[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)