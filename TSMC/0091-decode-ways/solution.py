class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        if int(s[0]) == 0: return 0
        dp[0] = 1
        if len(s) == 1: return dp[-1]
        
        # one digit
        if int(s[1]) != 0: dp[1] += dp[0]
        # two digit
        if 10 <= int(s[:2]) <= 26: dp[1] += 1

        if len(s) == 2: return dp[-1]

        for i in range(2, len(s)):
            # one digit
            if int(s[i]) != 0: dp[i] += dp[i-1]
            # two digit
            if 10 <= int(s[i-1:i+1]) <= 26: dp[i] += dp[i-2]
        
        return dp[-1]
