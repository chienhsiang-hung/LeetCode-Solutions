class QNode:
    def __init__(self, v=0, _next=None):
        self.value = v
        self.next = _next


class MyQueue:
    def __init__(self):
        self.root = None
        self.tail = None

    def push(self, x: int) -> None:
        if not self.root:
            self.root = QNode(x)
            self.tail = self.root
        else:
            self.tail.next = QNode(x)
            self.tail = self.tail.next
        
    def pop(self) -> int:
        output = self.root.value
        self.root = self.root.next
        return output

    def peek(self) -> int:
        return self.root.value

    def empty(self) -> bool:
        return not self.root


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()