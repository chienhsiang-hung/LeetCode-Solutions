'''
"race a car"
'raceacar'
r        r
 a      a
  c    c
   e  a
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([n.lower() for n in s if n.isalnum()])
        
        l = 0; r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
