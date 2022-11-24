# numbers of outer loop = len(nums)/2

# [88, 1, 87]:
# equal n will be sum(nums)/2

# it will be interger only (cuz: nums containing only positive integers, int+int==int)
# so the question is to find the sum of subset = sum(nums)/2

# similar to ...
# think as tree (graph) again and do BFS

from collections import defaultdict, deque
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums) / 2
        if goal % 1 != 0:
            return False

        visited = defaultdict(lambda: False)
        current = nums.pop()
        if current > goal:
            return False
        elif current == goal:
            return True
        visited[current] = True
        sub_list = [n for n in nums]
        queue = deque([
            (current, sub_list)
        ])
        
        while queue:
            current, sub_list = queue.popleft()
            for i, n1 in enumerate(sub_list):
                new_current = current + n1
                if new_current > goal:
                    continue

                if not visited[new_current]:
                    visited[new_current] = True
                    if new_current == goal:
                        return True

                    new_sub_list = []
                    for j, n2 in enumerate(sub_list):
                        if i != j: # avoid n1 itself
                            new_sub_list.append(n2)
                    if new_sub_list:
                        queue.append((new_current, new_sub_list))
        return False