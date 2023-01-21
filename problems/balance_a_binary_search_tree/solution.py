# traverse all nodes and build a new tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree_list = self.traverse_tree(root)
        
        def build_tree(l=0, r=len(tree_list)-1):
            if l > r:
                return None

            mid = (l+r)//2
            new_tree = TreeNode(tree_list[mid])
            new_tree.left = build_tree(l=l, r=mid-1)
            new_tree.right = build_tree(l=mid+1, r=r)
            return new_tree

        return build_tree()

    def traverse_tree(self, root: TreeNode) -> List:
        if not root: return []
        return self.traverse_tree(root.left) + [root.val] + self.traverse_tree(root.right)