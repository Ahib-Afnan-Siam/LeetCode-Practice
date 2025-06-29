# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = 0
        cur = root
        while cur:
            left_depth += 1
            cur = cur.left
        
        right_depth = 0
        cur = root
        while cur:
            right_depth += 1
            cur = cur.right
        
        if left_depth == right_depth:
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)