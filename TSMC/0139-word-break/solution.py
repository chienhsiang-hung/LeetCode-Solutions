class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set()
        max_word_len = 0
        for word in wordDict:
            wordSet.add(word)
            max_word_len = max(max_word_len, len(word))
        dp = [False] * (len(s) +1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i, i-max_word_len-1, -1):
                if j<0: continue

                if s[j:i+1] in wordSet and dp[j]:
                    dp[i+1] = True
        return dp[-1]
