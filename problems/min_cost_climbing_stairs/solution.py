# iterate through the cost list and 
# calculate the current(i) + min( (cost to i-1), (cost to i-2) )

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur = 0
        c1 = cur + cost[0]
        c2 = cur + cost[1]
        
        for i in range(2, len(cost)):
            cur = cost[i] + min(c1, c2)
            c1 = c2
            c2 = cur
        
        return min(c1, c2)
            
