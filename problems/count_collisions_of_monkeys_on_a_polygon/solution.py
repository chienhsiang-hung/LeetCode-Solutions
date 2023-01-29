class Solution:
    def monkeyMove(self, n: int) -> int:
        
        # def pow(i, n):
        #     if n == 0:
        #         return 1
        #     x = pow(i, n//2)
        #     x = x*x
        #     if n%2==1:
        #         x = x*i
        #     return x
        
        _mod = 10**9 + 7
        return (pow(2, n, _mod) - 2) % _mod
        