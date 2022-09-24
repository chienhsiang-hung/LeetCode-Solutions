class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        when there are duplicated strs in one, another one should have one at the same places
        '''
        if len(set(s)) == len(s) == len(set(t)) == len(t):
            return True
        
        s_map = dict()
        t_map = dict()
        for i, (s1, t2) in enumerate( zip(s, t) ):
            if s1 not in s_map:
                s_map[s1] = []
            if t2 not in t_map:
                t_map[t2] = []
            
            if len(s_map) != len(t_map):
                return False
            
            s_map[s1].append(i)
            t_map[t2].append(i)
        
        for (_, v1), (_, v2) in zip(s_map.items(), t_map.items()):
            if v1 != v2:
                return False
        return True
            