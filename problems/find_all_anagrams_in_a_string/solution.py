# 01 2345
# 0 12 345
# 01 23 45
# ...
# 0123 45

# abc
# cba ebabacd
# c bae babacd (i=3)
# ...
# cbaeba bac d (i=8)


from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        if len(p) > len(s):
            return output

        p_map = defaultdict(int)
        window = defaultdict(int)
        for i in range(len(p)):
            p_map[p[i]] += 1
            window[s[i]] +=1
        if window == p_map:
            output.append(0)

        for i in range(len(p), len(s)):
            window[ s[i-len(p)] ] -= 1

            # make sure these won't be something like {'c':0, 'b':1, 'a':1, 'e':1}
            if window[ s[i-len(p)] ] == 0:
                del window[ s[i-len(p)] ]

            window[ s[i] ] += 1


            if window == p_map:
                output.append(i-len(p)+1)
        
        return output