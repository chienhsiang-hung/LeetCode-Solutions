from collections import deque

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        new_words = []
        for word in words:
            current_word = [False]*26
            for chr_ in word:
                current_word[ord(chr_) - ord('a')] = True
            new_words.append( current_word )
        
        words = deque(new_words)
        output = 0
        while words:
            current = words.popleft()
            for word in words:
                if current == word:
                    output += 1
        
        return output
            