class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # generate hashmap
        word_bank = dict.fromkeys(s, 0)
        # calculate the amount of each _char
        for _char in s:
            word_bank[_char] += 1
        
        # calculate the len of the longest palindrome
        _len = 0
        has_one = 0
        for _, v in word_bank.items():
            _len += v//2 * 2
            if v %2 == 1: has_one = 1
        
        return _len + has_one