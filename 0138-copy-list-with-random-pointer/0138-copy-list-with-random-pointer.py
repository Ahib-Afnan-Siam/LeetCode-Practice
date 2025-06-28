"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        mapping = {}
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copied_node = mapping[current]
            if current.next:
                copied_node.next = mapping[current.next]
            else:
                copied_node.next = None
            if current.random:
                copied_node.random = mapping[current.random]
            else:
                copied_node.random = None
            current = current.next
        
        return mapping[head]