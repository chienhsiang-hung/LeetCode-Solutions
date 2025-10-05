from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1
        missing = len(t)

        l = best_l = 0
        best_r = float('inf')
        for i, char in enumerate(s):
            t_dict[char] -= 1
            if t_dict[char] >= 0:
                missing -= 1
            
            while missing == 0:
                t_dict[s[l]] += 1
                if t_dict[s[l]] > 0:
                    missing += 1
                    if i-l < best_r-best_l:
                        best_l = l
                        best_r = i
                l += 1
        return s[best_l:best_r+1] if best_r != float('inf') else ''
                    
