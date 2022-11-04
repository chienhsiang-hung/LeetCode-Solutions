# Try to make an O(n) solution with 2 pointer (1 iteration that's it)

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while left < right:
            left_in_v = s[left] in vowels
            right_in_v = s[right] in vowels
            if left_in_v and right_in_v:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif left_in_v and not right_in_v:
                right -= 1
            elif not left_in_v and right_in_v:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)
                