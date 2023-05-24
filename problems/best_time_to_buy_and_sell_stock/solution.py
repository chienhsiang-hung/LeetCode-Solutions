class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7, 1, 5, 3, 6, 4] = 5
        # [7, 6, 4] = 0
        # [5, 100, 1, 5] = 95
        # [1] = 0
        # [1, 2, 1, 2, 0, 1, 2] = 2
        
        # update min and check the max profit with previos stored profit
        
        # time: O(n), space: O(1)
        
        min_ = prices[0]
        profit = 0

        for p in prices[1:]:
            profit = max(profit, p-min_)
            min_ = min(min_, p)
            
        return profit