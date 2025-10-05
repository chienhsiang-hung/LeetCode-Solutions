class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for ch in s1:
            cnt1[ord(ch)-97] += 1
            
        if len(s1) > len(s2): return False
        for i in range(len(s1)):
            cnt2[ord(s2[i])-97] += 1
        if cnt1 == cnt2: return True
        if len(s1) == len(s2): return False

        for i in range(len(s1), len(s2)):
            cnt2[ord(s2[i-len(s1)])-97] -= 1
            cnt2[ord(s2[i])-97] += 1
            if cnt2 == cnt1: return True
        
        return False
