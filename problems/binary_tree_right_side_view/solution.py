# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS and get the last one in the same 'level'
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([
            [root]
        ])
        right_side = []
        
        # vertical iteration
        while queue:
            current_level = queue.popleft()
            right_side.append(current_level[-1].val) # add the last one in that level

            level_stack = []
            # horizontal iteration
            for node in current_level:
                for child in (node.left, node.right):
                    # skip None
                    if child:
                        level_stack.append(child)
            
            if level_stack: # to end the last                  
                queue.append(level_stack)
        
        return right_side
            
        


        