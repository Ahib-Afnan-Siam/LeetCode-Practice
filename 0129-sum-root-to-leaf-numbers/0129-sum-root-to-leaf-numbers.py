# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        total_sum = 0
        while stack:
            node, current_num = stack.pop()
            current_num = current_num * 10 + node.val
            if not node.left and not node.right:
                total_sum += current_num
            else:
                if node.right:
                    stack.append((node.right, current_num))
                if node.left:
                    stack.append((node.left, current_num))
        return total_sum