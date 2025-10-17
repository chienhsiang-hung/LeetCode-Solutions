import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        '''
        [1,10,2,2,-5,-1,100,101,3,5]
        [-1]
        [-1,-10] -> [-1] [10]
        [-1,-2] [10]
        [-1,-2,-2] [10] -> [-1,-2] [2,10]
        [5,-1,-2] [2,10]
        [5,1,-1,-2] [2,10] -> [5,1,-1] [2,2,10]
        [5,1,-1,-100] [2,2,10] -> [5,1,-1] [2,2,10,100]
        [5,1,-1,-101] [2,2,10,100] -> [5,1,-1,-2][2,10,100,101]

        [1,2,3]
        [-1]
        [-1,-2] -> [-1] [2]
        '''
        heapq.heappush(self.left, -num)
        
        if len(self.left) >= len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(
                self.left,
                -heapq.heappop(self.right)
            )

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0]) /2
        return -self.left[0] if len(self.left) > len(self.right) else self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
