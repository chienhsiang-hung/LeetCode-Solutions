class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1) 
        dp[0] = 0

        for i in range(1, amount+1):
            local_res = []
            for coin in coins:
                if (
                    i-coin >= 0 and
                    dp[i-coin] >= 0
                ):
                    local_res.append(1+dp[i-coin])
            
            if local_res: dp[i] = min(local_res)
        return dp[-1]

