'''
[3,2,2,4,1,4], 3
1, 16, 8: [3+2+2, 4+1, 4] == 3 left
1, 8, 4: [3, 2+2, 4, 1, 4] > 3 right
5, 8, 6: [3+2, 2+4, 1+4] == 3 left
5, 6, 5: [2+2, 2, 4+1, 4] > 3 ....

[1,2,3,1,1], 4
3, 8, 5: [1+2, 3+1, 1] < 4 turn left
3, 5, 4: [1+2, 3+1, 1] < 4 turn left
3, 4, 3: [1+2, 3, 1+1] < 4 ...
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        ans = r
        while l < r:
            mid = (l+r) // 2

            curr_stack = 0
            curr_day = 0
            for i, w in enumerate(weights):
                curr_stack += w
                if curr_stack > mid:
                    curr_day += 1
                    curr_stack = w
                elif curr_stack == mid:
                    curr_day += 1
                    curr_stack = 0
            if curr_stack > 0: curr_day += 1

            if curr_day == days:
                ans = min(ans, mid)
                r = mid
            elif curr_day > days: # turn right
                l = mid +1
            else: # turn left
                ans = min(ans, mid)
                r = mid
        return ans
