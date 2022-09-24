class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t or s == '':
            return True
        
        for _t in t:
            if _t == s[0]:
                s = s[1:]
                if s == '':
                    return True
        return s == ''