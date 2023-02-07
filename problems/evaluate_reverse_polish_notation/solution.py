# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# [10, 6, 9, 3]
# [10, 6, 9+3, -11]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i, stack = 0, []
        oprands = set(['+', '-', '*', '/'])
        while i < len(tokens):
            if tokens[i] not in oprands:
                stack.append(int(tokens[i]))
            else:
                r = stack.pop()
                l = stack.pop()
                if tokens[i] == '+':
                    stack.append(int(l+r))
                elif tokens[i] == '-':
                    stack.append(int(l-r))
                elif tokens[i] == '*':
                    stack.append(int(l*r))
                else:
                    stack.append(int(l/r))
            i += 1
        
        return stack[0]