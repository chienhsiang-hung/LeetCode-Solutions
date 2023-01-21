import heapq, math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-v for v in nums]
        heapq.heapify(nums)

        output = 0
        for _ in range(k):
            updated_v = -heapq.heappop(nums)

            output += updated_v
            heapq.heappush(nums, -math.ceil(updated_v/3))
        

        return output