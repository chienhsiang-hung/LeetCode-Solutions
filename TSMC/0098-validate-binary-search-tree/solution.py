# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverseTree(root):
            if not root.left and not root.right:
                return (True, root.val, root.val) # boolean, min, max

            
            if not root.left:
                rightResult = traverseTree(root.right)
                return (
                    rightResult[0] and rightResult[1] > root.val,
                    root.val,
                    rightResult[2]
                )
            
            if not root.right:
                leftResult = traverseTree(root.left)
                return (
                    leftResult[0] and leftResult[2] < root.val,
                    leftResult[1],
                    root.val
                )
            
            rightResult = traverseTree(root.right)
            leftResult = traverseTree(root.left)
            return (
                rightResult[0] and leftResult[0] and leftResult[2] < root.val < rightResult[1],
                leftResult[1],
                rightResult[2]
            )
            
        ans = traverseTree(root)
        return ans[0]
