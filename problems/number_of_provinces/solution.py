class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [False]*len(isConnected)

        def dfs(city):
            '''update visited'''
            if visited[city]: return
            visited[city] = True

            for i in range(len(isConnected)):
                if isConnected[city][i] == 1:
                    dfs(i)

            return
        
        # n*n matrix
        for i in range(len(isConnected)):
            if visited[i]: continue
            
            provinces += 1
            # DFS
            dfs(i)
        
        return provinces
                
