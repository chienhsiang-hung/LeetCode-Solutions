class Solution:
    def reverse(self, x: int) -> int:
        new_n = 0
        neg = True if x < 0 else False
        if neg: x = -1*x
        while x != 0:
            # check for 32-bit integer
            if new_n*10 + x%10 > 2**31-1: return 0
            new_n = new_n*10 + x%10
            x = x // 10
        return -1*new_n if neg else new_n