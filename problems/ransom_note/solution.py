class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_cnt = Counter()
        for mag in magazine:
            mag_cnt[mag] += 1
        
        for ran in ransomNote:
            # if ran not in mag_cnt:
            #     return False
            mag_cnt[ran] -= 1
            if mag_cnt[ran] < 0:
                return False
        return True