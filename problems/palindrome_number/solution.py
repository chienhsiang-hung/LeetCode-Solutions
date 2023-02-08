class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        ori = x
        new = 0
        while ori:
            new = new*10 + ori%10 # 0->1
            ori = ori // 10 # 121->12
            
        return x == new