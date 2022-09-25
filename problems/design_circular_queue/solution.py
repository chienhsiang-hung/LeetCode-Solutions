class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.data = [None]*k

    def enQueue(self, value: int) -> bool:
        for i, cell in enumerate(self.data):
            if cell == None:
                self.data[i] = value
                return True
        return False

    def deQueue(self) -> bool:
        if self.data[0] != None:
            self.data.pop(0)
            self.data.append(None)
            return True
        return False

    def Front(self) -> int:
        front = self.data[0]
        return front if front!=None else -1

    def Rear(self) -> int:
        data = [cell for cell in self.data if cell!=None]
        return data[-1] if data else -1

    def isEmpty(self) -> bool:
        return set(self.data) == {None}            

    def isFull(self) -> bool:
        return None not in self.data
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()