class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        _min = prices[0]
        
        for i in range(1, len(prices)):
            profit = max(prices[i] - _min, profit)
            _min = min(_min, prices[i])
        
        return profit

