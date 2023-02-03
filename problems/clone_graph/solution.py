"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        visited = set()
        graph = Node(node.val)
        queue = deque([node])
        node_map = {graph.val: graph}

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            for nb in current.neighbors:
                if nb.val not in node_map:
                    node_map[nb.val] = Node(nb.val)
                node_map[current.val].neighbors.append( node_map[nb.val] )
                queue.append( nb )
   
        return graph
            
            