# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        
        if root:
            return max(
                self.maxDepth(root.right, depth=depth+1),
                self.maxDepth(root.left, depth=depth+1)
            )