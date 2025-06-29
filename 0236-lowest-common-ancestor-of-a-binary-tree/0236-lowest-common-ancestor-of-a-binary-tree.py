# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        parent_map = {root: None}
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        current = p
        while current:
            ancestors.add(current)
            current = parent_map[current]
        
        current = q
        while current:
            if current in ancestors:
                return current
            current = parent_map[current]
        
        return None