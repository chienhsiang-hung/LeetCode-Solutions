import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for point in points:
            heapq.heappush(res, (
                (point[0]**2+point[1]**2)**(1/2),
                point
            ))
        ans = []
        while k:
            ans.append(
                heapq.heappop(res)[1]
            )
            k -= 1
        return ans
