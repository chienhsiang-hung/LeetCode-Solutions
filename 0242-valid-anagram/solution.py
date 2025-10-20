from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctr_s = Counter(s)
        ctr_t = Counter(t)

        return (
            len(ctr_s) == len(ctr_t) and
            all(ctr_s[i] == ctr_t[i] for i in ctr_s)
        )
