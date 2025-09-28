class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_map = dict()
        
        ans = 0
        max_count_c = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in c_map or not c_map[s[r]]:
                c_map[s[r]] = 1
            else:
                c_map[s[r]] += 1

            max_count_c = max(max_count_c, c_map[s[r]])
            while r+1-l - max_count_c > k:
                c_map[s[l]] -= 1
                max_count_c = max(max_count_c, c_map[s[l]])
                l += 1
            ans = max(ans, r+1-l)
        
        return ans
            
