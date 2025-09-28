class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            course_map[c].append(p)
        
        visited = set()
        def dfs(c):
            if not course_map[c]: return True
            if c in visited: return False
            visited.add(c)

            for p in course_map[c]:
                if not dfs(p): return False
            
            course_map[c] = []
            visited.remove(c)
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True
            


