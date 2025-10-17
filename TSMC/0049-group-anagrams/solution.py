from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        ct = [0] *26

        for s in strs:
            for c in s:
                ct[ord(c) - ord('a')] += 1
            ans[tuple(ct)].append(s)
            ct = [0] *26
        
        return list(ans.values())
