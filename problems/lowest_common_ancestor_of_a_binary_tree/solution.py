# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

# iterate through all nodes and record the parent
# find the common parent from bottom up
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes_q = deque([root])
        parent_dict = {root: None}
        pq_visited = 2
        while nodes_q:
            current = nodes_q.popleft()
            
            if current in (p, q):
                pq_visited -= 1
                if pq_visited == 0: break

            if current.left:
                nodes_q.append(current.left)
                parent_dict[current.left] = current
            if current.right:
                nodes_q.append(current.right)
                parent_dict[current.right] = current
        # current will be the lower one (either p or q) 
        higher = q if current == p else p
        # find the LCA
        lower_parents = set()
        while current: # if no current, lower_parents == []
            lower_parents.add(current)
            current = parent_dict[current]
            if current == higher:
                return current # first situ: LCA == one of p, q
        
        current = parent_dict[higher]
        while current not in lower_parents:
            current = parent_dict[current]
        
        return current
        


