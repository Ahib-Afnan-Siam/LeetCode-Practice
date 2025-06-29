# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        cur = root
        last_visited = None
        max_sum = -10**9
        return_map = {}
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack[-1]
                if node.right and node.right != last_visited:
                    cur = node.right
                else:
                    node = stack.pop()
                    left_val = 0
                    right_val = 0
                    if node.left:
                        left_val = max(0, return_map[node.left])
                    if node.right:
                        right_val = max(0, return_map[node.right])
                    total = node.val + left_val + right_val
                    if total > max_sum:
                        max_sum = total
                    ret_val = node.val + max(left_val, right_val)
                    return_map[node] = ret_val
                    last_visited = node
                    cur = None
        return max_sum