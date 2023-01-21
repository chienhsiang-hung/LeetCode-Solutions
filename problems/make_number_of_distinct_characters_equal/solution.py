from collections import Counter
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        word1_map = Counter(word1)
        word1_dn = 0
        for k in word1_map.keys():
            word1_dn += 1
        word2_map = Counter(word2)
        word2_dn = 0
        for k in word2_map.keys():
            word2_dn += 1

        for chr1 in set(word1):
            for chr2 in set(word2):
                # chr2 added in word1
                word1_map[chr2] += 1
                if word1_map[chr2] == 1:
                    word1_dn += 1
                word2_map[chr2] -= 1
                if word2_map[chr2] == 0:
                    word2_dn -= 1
                
                # chr1 added in word2
                word2_map[chr1] += 1
                if word2_map[chr1] == 1:
                    word2_dn += 1
                word1_map[chr1] -= 1
                if word1_map[chr1] == 0:
                    word1_dn -= 1


                # check
                if word1_dn == word2_dn: return True


                # chr2 removed from word1
                word1_map[chr2] -= 1
                if word1_map[chr2] == 0:
                    word1_dn -= 1
                word2_map[chr2] += 1
                if word2_map[chr2] == 1:
                    word2_dn += 1

                # chr1 removed from word2
                word2_map[chr1] -= 1
                if word2_map[chr1] == 0:
                    word2_dn -= 1
                word1_map[chr1] += 1
                if word1_map[chr1] == 1:
                    word1_dn += 1

        return False
                