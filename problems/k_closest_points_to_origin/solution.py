import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        for point in points:
            output.append((
                abs( (point[0]**2+point[1]**2) ** (1/2) ),
                point
            ))
        heapq.heapify(output)
        return [v2 for v1, v2 in heapq.nsmallest(k, output)]