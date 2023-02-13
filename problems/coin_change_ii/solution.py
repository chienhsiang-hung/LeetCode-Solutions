# https://www.youtube.com/watch?v=DJ4a7cmjZY0&t=192s

#             0   1   2   3   4   5   6
# []          1   0   0   0   0   0   0
# [2]         1   0   1  `0   1   0   1
# [2,3]       1   0   1   1   1   1   2
# [2,3,5]     1   0   1   1   1   2   2
# [2,3,5,7]   1   0   1   1   1   2   2

# dp[r][c] = dp[r-1][c] + dp[r][c-coins[r-1]]

#         0   1   2   3   4   5
# []      1   0 
# [1]     1   1
# [1,2]   1   
# [1,2,5] 1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)

        dp = [
            [1]+[0]*(amount) for _ in range(len(coins)+1)
        ]
        for c in range(1, amount+1):
            for r in range(1, len(coins)+1):
                if coins[r-1] > c:
                    dp[r][c] = dp[r-1][c]
                    continue
                if coins[r-1] == c:
                    dp[r][c] = dp[r-1][c] + 1
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-coins[r-1]]
        
        return dp[-1][-1]
                
                
                

        
        