class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1

            if 0 <= l <= r < len(s) and s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True