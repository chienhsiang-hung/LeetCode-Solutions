"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clone = {node.val: Node(node.val)}
        for nb in node.neighbors:
            clone[nb.val] = Node(nb.val)
            clone[node.val].neighbors.append(clone[nb.val])
        q = deque(node.neighbors)
        while q:
            cur_vis = q.popleft()
            if not clone[cur_vis.val].neighbors:
                for nb in cur_vis.neighbors:
                    if nb.val not in clone:
                        clone[nb.val] = Node(nb.val)
                    clone[cur_vis.val].neighbors.append(clone[nb.val])
                    if not clone[nb.val].neighbors:
                        q.append(nb)
        return clone[node.val]
            
