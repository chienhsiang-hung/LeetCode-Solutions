class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        p1 = prices[0] # p1: buy price
        for p2 in prices[1:]: # p2: sell price
            if p2 > p1:
                profit += p2-p1
            # when p2 <= p1, update p1
            p1 = p2
        return profit
                
            