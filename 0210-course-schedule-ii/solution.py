from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        [[1,0], [2,0], [3,1], [3,2]]

        1:0
        0:1

        1:0,2
        2:0

        [[1,0]]
        '''
        courses = defaultdict(list)
        for c, p in prerequisites:
            courses[c].append(p)
        
        ans = []
        ans_added = set()

        def findPre(c):
            if c in vis:
                return False
            vis.add(c)
            if not courses[c] and c not in ans_added:
                ans.append(c)
                ans_added.add(c)
                return True
            while courses[c]:
                curr_c = courses[c].pop()
                if not findPre(curr_c): return False
                vis.remove(curr_c)
            if c not in ans_added:
                ans.append(c)
                ans_added.add(c)
            return True
                

        for c in range(numCourses):
            if not courses[c] and c not in ans_added:
                ans.append(c)
                ans_added.add(c)
            else:
                vis = set()
                if not findPre(c):
                    return []
        return ans
