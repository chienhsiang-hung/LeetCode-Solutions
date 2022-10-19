# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. accu from root
# 2. then accu from root.left adn root.right  
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.targetSum = targetSum
        self.nums = 0
        def accu_to_tar(root, curr_num=0):
            if not root:
                return 0

            curr_num += root.val
            if curr_num == self.targetSum:
                self.nums += 1
            accu_to_tar(root.left, curr_num)
            accu_to_tar(root.right, curr_num)
        
        # BFS
        nodes = [root]
        while nodes:
            curr_node = nodes.pop(0)
            accu_to_tar(curr_node)
            if curr_node:
                nodes.append(curr_node.left)
                nodes.append(curr_node.right)
        return self.nums
            
            
            