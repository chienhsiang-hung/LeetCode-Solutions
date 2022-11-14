import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-item for item in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            big1 = heapq.heappop(stones)
            big2 = heapq.heappop(stones)
            heapq.heappush(stones, big1-big2)
        
        return -stones[0]
            