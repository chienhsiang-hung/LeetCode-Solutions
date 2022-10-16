from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pair_map = defaultdict(int)

        for word in words:
            pair_map[word] += 1

        pldr_len = 0
        centre_gg = False
        # Distinguish 
        for word in words:
            k1 = word
            k2 = word[::-1]
            
            if k1 == k2:
                pldr_len += pair_map[word] //2 *2 *2
                pair_map[word] = pair_map[word] %2
                if not centre_gg and pair_map[word] ==1:
                    pldr_len += 2
                    centre_gg = True
            else:
                pldr_len += min(pair_map[k1], pair_map[k2]) *2 *2
                pair_map[k1] = 0
                pair_map[k2] = 0
        
        return pldr_len
        