"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        res = Node(node.val)

        q = deque([node])

        clones = {node : res}

        while q:
            original_node = q.popleft()

            for neighbor in original_node.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                clones[original_node].neighbors.append(clones[neighbor])
        
        return clones[node]

