# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from the example we can see the subRoot should be the bottom of the root
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        def compare_tree(node1, node2):
            if not node1 and not node2: return True
            elif not node1 and node2: return False
            elif node1 and not node2: return False

            if node1.val != node2.val: return False

            return compare_tree(node1.left, node2.left) and compare_tree(node1.right, node2.right)

        if root.val == subRoot.val:
            return compare_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)