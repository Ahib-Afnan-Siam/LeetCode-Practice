# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum)]
        while stack:
            node, remaining = stack.pop()
            if not node.left and not node.right and node.val == remaining:
                return True
            if node.left:
                stack.append((node.left, remaining - node.val))
            if node.right:
                stack.append((node.right, remaining - node.val))
        return False