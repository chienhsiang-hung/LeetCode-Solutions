'''
[7,2,5,10,8], k=2
10, 32, 21: [7+2+5, 10+8], 18, 2 -> turn left
10, 18, 14: [7+2+5, 10, 8], 14, 3 -> turn right
15, 18, 16: [7+2+5, 10, 8], 14, 3 -> turn right
17, 18, 17: [7+2+5, 10, 8], 14, 3 -> turn right

[1,2,3,4,5], k=5
5, 15, 10: [1+2+3+4, 5], 10, 2 < k -> turn left
5, 10, 7: [1+2+3, 4, 5], 6, 3 < k -> turn left
5, 7, 6: [1+2+3, 4, 5], 6, 3 < k -> turn left
5, 6, 5: [1+2, 3, 4, 5] 5, 4 < k
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        min_sum = r
        while l < r:
            mid = (l+r) // 2

            curr_load = 0
            curr_day = 0
            local_max = 0
            for i, n in enumerate(nums):
                curr_load += n
                if curr_load > mid:
                    local_max = max(curr_load-n, local_max)
                    curr_load = n
                    curr_day += 1
                elif curr_load == mid:
                    local_max = max(curr_load, local_max)
                    curr_load = 0
                    curr_day += 1
            if curr_load:
                local_max = max(curr_load, local_max)
                curr_day += 1

            if local_max <= mid and curr_day <= k:
                min_sum = min(min_sum, local_max)
            
            if curr_day < k:
                r = mid
            elif curr_day > k:
                l = mid +1
            else:
                r = mid
        return min_sum

