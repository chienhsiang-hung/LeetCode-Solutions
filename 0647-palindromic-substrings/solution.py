'''
abbaaa    
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        # one ch
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        if len(s) < 2: return ans
        # two chs
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans

                
