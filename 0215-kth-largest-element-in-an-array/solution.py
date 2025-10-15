import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        heapq.heapify(res)
        for n in nums:
            heapq.heappush(res, -n)
        
        while k:
            ans = -heapq.heappop(res)
            k -= 1
        return ans
