# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def tree_to_list(root) -> list:
            if not root:
                return []

            return tree_to_list(root.right) + [root.val] + tree_to_list(root.left)
        
        tree_list = tree_to_list(root)
        return tree_list[-k]