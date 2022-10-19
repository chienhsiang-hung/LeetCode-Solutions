# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], _min=0, _max=0) -> int:
        
        self.max = 0

        def height(root):
            if not root:
                return 0
            
            left_h = height(root.left)
            right_h = height(root.right)
            self.max = max(self.max, left_h+right_h)
            return max(left_h, right_h)+1
        
        height(root)
        return self.max