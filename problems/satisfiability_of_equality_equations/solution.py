class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # ["a==b","b!=a"] False
        # ["b==a","a==b"] True
        # ["a==b","b==c","c!=a"] False
        # ["a!=a"] False
        # ["a==b","a==c","c!=b"] False
        # ["a==b","c==a","c!=b"] False
        
        
        parent = [i for i in range(26)]
        
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        
        for e in equations:
            a = ord(e[0]) % 97
            b = ord(e[3]) % 97
            eq = e[1]
            if eq == '=':
                parent[find(a)] = find(b)
        
        for e in equations:
            a = ord(e[0]) % 97
            b = ord(e[3]) % 97
            eq = e[1]
            if eq == '!' and find(a) == find(b):
                return False
        
        return True
        
                

                
            