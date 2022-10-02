# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [brute force]
#   find the route to p, find the route to q
#   find the LCA through the list
#   (in the same tree: they must have a CA)
# [think about BST]
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        if p.val < q.val:
            small, big = p.val, q.val
        else:
            small, big = q.val, p.val

        while current:
            # if one of p,q is LCA
            if current.val == small:
                return current
            elif current.val == big:
                return current


            if small < current.val < big:
                return current
            # go left
            elif small < big < current.val:
                current = current.left
            # go right
            else:
                current = current.right


