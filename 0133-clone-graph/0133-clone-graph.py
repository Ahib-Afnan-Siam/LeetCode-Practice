from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone_dict = {}
        queue = deque([node])
        clone_dict[node] = Node(node.val, [])
        
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in clone_dict:
                    clone_dict[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clone_dict[current].neighbors.append(clone_dict[neighbor])
        
        return clone_dict[node]