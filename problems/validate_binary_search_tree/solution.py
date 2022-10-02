# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# check .left < current < .right
# need to check if a right grandchilde of a left child is smaller than the current node 
class Solution:
    def isValidBST(self, root: Optional[TreeNode], _max=None, _min=None) -> bool:
        if not root:
            return True

        if root.left:
            if root.left.val >= root.val:
                return False
            if _min:
                if root.left.val <= _min:
                    return False
        if root.right:
            if root.right.val <= root.val:
                return False
            if _max:
                if root.right.val >= _max:
                    return False

        return self.isValidBST(root.left, _max=root.val, _min=_min) and self.isValidBST(root.right, _max=_max, _min=root.val)
        
        