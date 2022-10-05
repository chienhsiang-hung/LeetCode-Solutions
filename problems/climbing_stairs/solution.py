# Fibonacci (adjustment)

class Solution:
    def climbStairs(self, n: int, a=1, b=1, i=2) -> int:
        if n == 1:
            return b
        if n == i:
            return a+b
        
        return self.climbStairs(n, a=b, b=a+b, i=i+1)