# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        inorder_map = dict()
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        inorder_visited = [False] * len(inorder)

        def build():
            root = TreeNode(preorder.popleft())
            inorder_visited[ inorder_map[root.val] ] = True
            
            if (
                inorder_map[root.val] -1 >= 0 and 
                not inorder_visited[
                    inorder_map[root.val] -1
                ]
            ):
                root.left = build()
            else:
                root.left = None
            
            if (
                inorder_map[root.val] +1 < len(inorder) and 
                not inorder_visited[
                    inorder_map[root.val] +1
                ]
            ):
                root.right = build()
            else:
                root.right = None

            return root

        return build()