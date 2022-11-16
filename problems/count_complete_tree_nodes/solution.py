# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# utilize the cherecteristic of The Complete Tree
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_height(root):
            if not root:
                return 0
            return 1 + get_height(root.left)
        
        left_height = get_height(root.left)
        right_height = get_height(root.right)

        # left full
        if left_height == right_height:
            return 2**(left_height)-1 + 1 + self.countNodes(root.right)
        # right full
        else:
            return 2**(right_height)-1 + 1 + self.countNodes(root.left)