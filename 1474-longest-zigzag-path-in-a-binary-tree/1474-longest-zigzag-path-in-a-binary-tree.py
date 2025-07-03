# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        res_map = {}
        max_ans = 0
        for node in reversed(order):
            left_val = 0
            right_val = 0
            if node.left:
                left_val = 1 + res_map[node.left][1]
            if node.right:
                right_val = 1 + res_map[node.right][0]
            res_map[node] = (left_val, right_val)
            if left_val > max_ans:
                max_ans = left_val
            if right_val > max_ans:
                max_ans = right_val
        
        return max_ans