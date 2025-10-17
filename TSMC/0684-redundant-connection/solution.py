class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            if par[n] == n:
                return n
            return find(par[n])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        
