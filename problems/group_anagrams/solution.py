# O(n*mlogm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for _str in strs:
            sted = sorted(_str)
            map[tuple(sted)].append(_str)
        return map.values()
                
