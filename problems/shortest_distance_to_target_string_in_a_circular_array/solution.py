# 2 pointer

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        steps = 0
        
        while steps <= len(words)/2:
            # go right
            if words[
                (startIndex + steps) % len(words)
            ] == target:
                return steps
            
            # go left
            if words[
                (startIndex - steps) % len(words)
            ] == target:
                return steps
            
            steps += 1
        
        return -1
            