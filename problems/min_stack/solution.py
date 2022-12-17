class MinStack:
    def __init__(self):
        #[(int, min_at_the_moment), (int, min_at_the_moment), ...]
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append( (val, val) )
        else:
            self.stack.append(
                (val, min(val, self.stack[-1][1]))
            )

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()