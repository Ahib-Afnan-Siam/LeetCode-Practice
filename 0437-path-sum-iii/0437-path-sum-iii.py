from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        stack = []
        count = 0
        stack.append((0, root, 0))
        
        while stack:
            cmd, node, parent_current = stack.pop()
            current_sum = parent_current + node.val
            
            if cmd == 1:
                prefix_sum[current_sum] -= 1
                if prefix_sum[current_sum] == 0:
                    del prefix_sum[current_sum]
            else:
                count += prefix_sum.get(current_sum - targetSum, 0)
                prefix_sum[current_sum] += 1
                stack.append((1, node, parent_current))
                if node.right:
                    stack.append((0, node.right, current_sum))
                if node.left:
                    stack.append((0, node.left, current_sum))
        
        return count