# https://www.youtube.com/watch?v=Hr5cWUld4vU

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val] # we have at least one node as input

        def dfs(root):
            if not root:
                return 0
            
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            
            # spliting
            result[0] = max(result[0], root.val+left_max+right_max)
            # not spliting
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return result[0]