### Python| Intuitive Solution O(1) Time O(n) Memory | In-order Traversal ###

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.tree_list = self.in_order_traversal(root)
        self.pos = -1

    def next(self) -> int:
        '''Given the call of next() will always be valid'''
        self.pos += 1
        return self.tree_list[self.pos]
        
    def hasNext(self) -> bool:
        if self.pos +1 < len(self.tree_list):
            return True
        return False
    
    def in_order_traversal(self, root):
        if not root:
            return []
        return self.in_order_traversal(root.left) + [root.val] + self.in_order_traversal(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()