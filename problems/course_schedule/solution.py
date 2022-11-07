# if there is a loop, it won't be possible to finish all courses

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        pre_cs_list = [0] * numCourses

        for next_c, pre_c in prerequisites:
            graph[pre_c].append(next_c)
            pre_cs_list[next_c] += 1
            
        q = deque()
        # check independent cources
        for i in range(numCourses):
            if pre_cs_list[i] == 0:
                q.append(i)
        

        ans = []    
        while q:
            curr = q.popleft()
            ans.append(curr)

            for next_c in graph[curr]:

                pre_cs_list[next_c] -= 1
                if pre_cs_list[next_c] == 0:
                    q.append(next_c)
        return len(ans) == numCourses

            
            
            