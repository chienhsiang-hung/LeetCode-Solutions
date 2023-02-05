# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # BFS
        output = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if not curr:
                output.append('null')
                continue
            output.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        return ','.join(output)
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'null': return None        
        
        data = deque(data.split(','))
        head = TreeNode(int(data.popleft()))
        tqueue = deque([head])
        while data:
            curr = tqueue.popleft()
            # left
            if data:
                left = int(v) if (v:=data.popleft()) != 'null' else None
                if left != None:
                    curr.left = TreeNode(left)
                    tqueue.append(curr.left)
            if data:
                right = int(v) if (v:=data.popleft()) != 'null' else None
                if right != None:
                    curr.right = TreeNode(right)
                    tqueue.append(curr.right)
        return head
                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))