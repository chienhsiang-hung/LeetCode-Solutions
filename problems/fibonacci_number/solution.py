# bottom-up dynamic programming

class Solution:
    def fib(self, n: int, a=0, b=1, i=2) -> int:
        if n==0: return a
        elif n==1: return b
        
        if n == i:
            return a+b

        return self.fib(n, a=b, b=b+a, i=i+1)

        

        