# [-1], [3] => m=2
# add: 4 >2 => [-1], [3,4] => m=3
# add: 5 >3
#   but big is too long => [-1,-3], [4,5] => m=6.5

import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        # base case for 1 ele
        if not self.small:
            self.small.append(-num)
            return

        # base case for 2 ele
        if not self.big:
            if num < -self.small[0]:
                self.big.append(-self.small.pop())
                self.small.append(-num)
            else:
                self.big.append(num)
            return
        
        mid = self.findMedian()
        # right is longer and you add to right
        if len(self.big) > len(self.small) and num >= mid:
            heapq.heappush(self.small, -heapq.heappop(self.big))
            heapq.heappush(self.big, num)
        # left is longer and you add to left
        elif len(self.small) > len(self.big) and num < mid:
            heapq.heappush(self.big, -heapq.heappop(self.small))
            heapq.heappush(self.small, -num)
        elif num >= mid:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)
        
    def findMedian(self) -> float:
        '''O(1)'''
        if len(self.small) == len(self.big):
            return (-self.small[0]+self.big[0]) /2
        if len(self.small) > len(self.big):
            return -self.small[0]
        return self.big[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()