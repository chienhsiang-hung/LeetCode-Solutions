from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''Example 1: Input: s = "ababcbacadefegdehijhklij"'''
        last_i = defaultdict(int)
        for i, c in enumerate(s):
            last_i[c] = i
        
        l = 0
        r = last_i[s[0]]
        res = []
        for i, c in enumerate(s):
            if i == r:
                res.append(i-l+1)
                l = i+1

                if l == len(s): break
                
                r = last_i[s[i+1]]
                continue

            r = max(r, last_i[c])
        return res
