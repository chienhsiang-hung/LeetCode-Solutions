class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        word_dict = {'a':0, 'b':0, 'c':0}
        for ss in s:
            word_dict[ss] += 1
        if not all(v >= k for v in word_dict.values()): return -1
        
        limit = word_dict.copy()
        for ks in limit.keys():
            limit[ks] -= k
        # find the longest string from the middle where non value exceed the above map
        if all(v == 0 for v in word_dict.values()): return len(s)
        window = {'a':0, 'b':0, 'c':0}
        l = r = 0
        max_len = 0
        while r < len(s):
            # add and mv right
            window[s[r]] += 1
            r += 1
            # del and mv left
            while window[s[r-1]] > limit[s[r-1]] and l<=r:
                window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l)
        return len(s) - max_len