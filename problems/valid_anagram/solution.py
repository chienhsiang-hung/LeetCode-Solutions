class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_count_s = Counter()
        word_count_t = Counter()
        for ss in s:
            word_count_s[ss] += 1
        for tt in t:
            word_count_t[tt] += 1
        
        return word_count_s == word_count_t