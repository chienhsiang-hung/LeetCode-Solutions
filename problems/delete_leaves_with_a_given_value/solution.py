# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int, parent=None, pos='root') -> Optional[TreeNode]:
        if not root: return

        self.removeLeafNodes(root.left, target, root, 'left')
        self.removeLeafNodes(root.right, target, root, 'right')

        if root.val == target:
            # check if it's leaf
            if not root.left and not root.right:
                if pos == 'left':
                    parent.left = None
                elif pos == 'right':
                    parent.right = None
                else:
                    return None
            
        return root
        