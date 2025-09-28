class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_map = dict()
        
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in c_map or not c_map[s[r]]:
                c_map[s[r]] = 1
            else:
                c_map[s[r]] += 1

            while r+1-l - max(c_map.values()) > k:
                c_map[s[l]] -= 1
                l += 1
            ans = max(ans, r+1-l)
        
        return ans
            
