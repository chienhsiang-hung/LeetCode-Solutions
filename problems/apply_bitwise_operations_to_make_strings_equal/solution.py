# (1, 0) -> (1, 1)
# (0, 0) -> (0, 0)
# (1, 1) -> (1, 0)
# (0, 1) -> (1, 1)

# all 0 stays 0
# only 1, you can make 0
# 1, 0 you can make all 1

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # all 0 in target
        if '1' not in target:
            return '1' not in s
        
        # all 1 in target
        elif '0' not in target:
            return '1' in s
        
        # 0 and 1 in target
        else:
            return not ('1' not in s)