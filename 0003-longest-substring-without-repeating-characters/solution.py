class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {} # key c, v i
        maxLength = 0

        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = i
                maxLength = max(maxLength, len(charMap))
            else:
                curCi = charMap[s[i]]
                for k in list(charMap.keys()):
                    if charMap[k] <= curCi:
                        charMap.pop(k)
                charMap[s[i]] = i
        return maxLength
