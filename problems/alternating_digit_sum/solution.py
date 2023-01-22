class Solution:
    def alternateDigitSum(self, n: int) -> int:
        output = 0
        i = 0
        n = str(n)
        
        while i+1 < len(n):
            output += int(n[i])
            output -= int(n[i+1])
            
            i += 2
        
        if i+1 == len(n):
            output += int(n[i])
        
        return output