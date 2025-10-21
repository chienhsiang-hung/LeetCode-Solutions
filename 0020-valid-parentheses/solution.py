'''
"([]{()[]})"
( ; )
([ ; ])
([] ; )
([]{ ; })
([]{( ; )})
([]{() ; })
'''
class Solution:
    def isValid(self, s: str) -> bool:
        par = {'(':')', '[':']', '{':'}'}
        
        waitlist = []
        for ch in s:
            if ch in par:
                waitlist.append(par[ch])
                continue

            if not waitlist: return False
            if ch == waitlist[-1]:
                waitlist.pop()
            else:
                return False
                
        return len(waitlist) == 0
