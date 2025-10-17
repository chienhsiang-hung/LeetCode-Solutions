from collections import defaultdict, deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1 and r!=c:
                    adj_dict[r].append(c)

        visited = set(); p = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            visited.add(i)
            q = deque(adj_dict[i])
            while q:
                city = q.popleft()
                if city in visited:
                    continue
                visited.add(city)
                for j in adj_dict[city]:
                    q.append(j)
            
            p += 1
        return p
