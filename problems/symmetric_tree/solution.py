# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# flip one part (let's say the left) of tree to see if they are identical
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: return True
        elif not root.left: return False
        elif not root.right: return False

        def flip_tree(node):
            if not node:
                return None
            node.left, node.right = flip_tree(node.right), flip_tree(node.left)
            
            return node

        root.left = flip_tree(root.left)

        def compare_tree(n1, n2):
            if n1 == n2 == None: return True
            elif not n1: return False
            elif not n2: return False
            
            if n1.val != n2.val: return False

            return compare_tree(n1.left, n2.left) and compare_tree(n1.right, n2.right)
        
        
        return compare_tree(root.left, root.right)


        