# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# create a map to record the levels: to nodes
# then join the nodes together
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_map = dict()
        def BFS_record_level(node, i=0):
            if not node:
                return
            if i not in level_map:
                level_map[i] = [node.val]
            else:
                level_map[i].append(node.val)
            BFS_record_level(node.left, i+1)
            BFS_record_level(node.right, i+1)
            return
        
            # return [(node.val, i)] + BFS_record_level(node.left, i+1) + BFS_record_level(node.right, i+1)
        BFS_record_level(root)
        return [v for _, v in level_map.items()]

