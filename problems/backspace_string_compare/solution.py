class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        i = 0
        for ss in s:
            if ss != '#':
                new_s.append(ss)
            elif ss == '#' and len(new_s) > 0:
                new_s.pop()
        
        new_t = []
        for tt in t:
            if tt != '#':
                new_t.append(tt)
            elif tt == '#' and len(new_t) > 0:
                new_t.pop()
        
        return new_s == new_t