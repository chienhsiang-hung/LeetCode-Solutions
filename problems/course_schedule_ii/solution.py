from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for next_c, pre_c in prerequisites:
            graph[pre_c].append(next_c)
            in_degree[next_c] += 1
            
        BFS_q = deque()
        for cs in range(numCourses):
            if in_degree[cs] == 0:
                BFS_q.append(cs)
        
        ans = []
        while BFS_q:
            curr = BFS_q.popleft()
            ans.append(curr)
            for next_c in graph[curr]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    BFS_q.append(next_c)
        
        return ans if len(ans)==numCourses else []