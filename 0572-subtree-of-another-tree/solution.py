# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
   def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       def checkSameTree(tree1, tree2):
           q1 = deque([tree1])
           q2 = deque([tree2])
           while q1 and q2:
               cur1 = q1.popleft()
               cur2 = q2.popleft()
               if (not cur1 and cur2) or (not cur2 and cur1):
                   return False
               if not cur1 and not cur2:
                   continue
               if cur1.val != cur2.val:
                   return False
               q1.append(cur1.left)
               q1.append(cur1.right)
               q2.append(cur2.left)
               q2.append(cur2.right)
           return True
       main_q = deque([root])
       while main_q:
           cur_main_node = main_q.popleft()
           if not cur_main_node: continue
           if checkSameTree(cur_main_node, subRoot):
               return True
           main_q.append(cur_main_node.left)
           main_q.append(cur_main_node.right)
       return False
