'''
s = ""ADOBECODEBANC", t = "ABC"
ADOBEC
DOBECODEBA
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countC = dict()
        for c in t:
            if c not in countC:
                countC[c] = 1
            else:
                countC[c] += 1
        needed = len(t)
        
        l = 0
        window_size = float('inf')
        ans = ''
        for i, c in enumerate(s):
            if c in countC:
                countC[c] -= 1
                if countC[c] >= 0:
                    needed -= 1
            
            if needed == 0 and i-l+1 < window_size:
                ans = s[l:i+1]
                window_size = i+1-l
            
            while needed == 0:
                if i-l+1 < window_size:
                    ans = s[l:i+1]
                    window_size = i+1-l

                if s[l] in countC:
                    countC[s[l]] += 1
                    if countC[s[l]] > 0:
                        needed += 1
                l += 1
        
        return ans
