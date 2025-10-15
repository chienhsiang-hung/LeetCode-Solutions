# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node.left and not node.right:
                return node.val, node.val # join, split
            if not node.left:
                childRight = traverse(node.right)
                return max(childRight[0]+node.val, node.val), max(childRight)
            if not node.right:
                childLeft = traverse(node.left)
                return max(childLeft[0]+node.val, node.val), max(childLeft)
            
            childRight = traverse(node.right)
            childLeft = traverse(node.left)
            return (
                max(
                    node.val,
                    node.val + max(childRight[0], childLeft[0])
                ),
                max([
                    max(childRight),
                    max(childLeft),
                    node.val + childRight[0] + childLeft[0]
                ])
            )

        ans = traverse(root)
        return max(ans)
