class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        charSet = set()
        l = 0
        maxL = 0

        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxL = max(maxL, r+1-l)
            else:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                    
                l += 1
        return max(maxL, r+1-l)
