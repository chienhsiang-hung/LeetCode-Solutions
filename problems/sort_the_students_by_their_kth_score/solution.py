# divide and conquer
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        if not score: return score
        if len(score) == 1: return score
        
        mid = len(score) // 2
        
        left = self.sortTheStudents(score[:mid], k)
        right = self.sortTheStudents(score[mid:], k)
        
        return self.merge(left, right, k)
    
    def merge(self, left, right, k):
        '''
        @left: score-lists
        @right: score-lists
        '''
        if len(left) <= len(right):
            short, long = left, right
        else:
            short, long = right, left
        
        output = []
        l, r = 0, 0
        while l < len(short) and r < len(long) and short and long:
            if short[l][k] < long[r][k]:
                output.append(long[r])
                r += 1
            else:
                output.append(short[l])
                l += 1
        if l < len(short):
            output += short[l:]
        if r < len(long):
            output += long[r:]
        
        return output
            
            