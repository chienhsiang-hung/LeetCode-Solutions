# 0, 0      0
# 1, 1      1
# 2, 10     1
# 3, 11     2
# 4, 100    1
# 5, 101    2
# 6, 110    2
# 7, 111    3
# 8, 1000   1
# 9, 1001   2
# 10,1010   2
# 11,1011   3

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        def solve(n):
            if n == 0:
                output.append(0)
                return deque([0]), 0
            
            last, ones = solve(n-1)
            i = len(last)-1
            while i >= 0:
                last[i] += 1
                # 0 -> 1
                if last[i] == 1:
                    ones += 1
                    break
                # 1 -> 2
                last[i] = 0
                ones -= 1
                i -= 1

            if last[0] == 0:
                last.appendleft(1)
                ones += 1
            output.append(ones)
            return last, ones
        
        solve(n)
        return output
                