class Solution:
    def hasSameDigits(self, s: str) -> bool:
        stack = [[int(n) for n in list(s)]]
        while len(stack[0]) > 2:
            cur = stack.pop()
            new_str = []
            for i in range(len(cur)-1):
                new_str.append(
                    (cur[i] + cur[i+1]) % 10
                )
            stack.append(new_str)
        return stack[0][0] == stack[0][1]
