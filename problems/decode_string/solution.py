# record the num
# num * []
# iterate again...

class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s:
            return s

        decoded = []
        i = 0
        digit = []
        while i < len(s):
            if s[i].isdigit():
                digit.append( s[i] )

                if s[i+1] == '[':
                    start = i+1
                    end = start+1
                    level = 1
                    while level > 0:
                        if s[end] == '[':
                            level += 1
                        if s[end] == ']':
                            level -= 1
                        end += 1
                    decoded.append(
                        int(''.join(digit)) * s[start+1:end-1]
                    )
                    i = end-1
                    digit = []
            else:
                decoded.append(s[i])
            i += 1
        return self.decodeString(''.join(decoded))