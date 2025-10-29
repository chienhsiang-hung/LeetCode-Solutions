'''
babadabccba
b a (0,11)
b b, a a (0,10) (1,11)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPLD(l, r):
            while l <= r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)): # i=1
            for j in range(i+1): # j=0 
                if checkPLD(j, len(s)-i+j-1): return s[j:len(s)-i+j]
