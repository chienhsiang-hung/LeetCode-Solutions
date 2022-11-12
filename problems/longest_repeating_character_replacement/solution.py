# left and right
# use right pointer to walk through the s
#   record the current_window_size and the max_chr
#   when current_window_size - max_chr > k
#       move left to the next next
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        chr_bank = defaultdict(int)
        max_window = 0
        while right < len(s):
            chr_bank[ s[right] ] += 1
            window = 1 + right - left

            # when there is no room to change the chr
            while window - max(chr_bank.values()) > k:
                if window-1 > max_window:
                    max_window = window-1
                chr_bank[ s[left] ] -= 1
                left += 1
                window -= 1
            right += 1
        if right-left > max_window:
            max_window = right-left
        return max_window
                
            