class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        output = strs[0]
        if len(strs) == 1:
            return output
        for _str in strs[1:]:
            if _str == '':
                return ''
            for i, _chr in enumerate(_str):
                if i > len(output)-1:
                    break
                if _chr != output[i]:
                    output = output[:i]
                    break
            if len(_str) < len(output):
                output = output[:i+1]
            if output == '':
                return output
        return output
                
            