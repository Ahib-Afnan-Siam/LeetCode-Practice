# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, -10**5)]
        count = 0
        while stack:
            node, curr_max = stack.pop()
            if node.val >= curr_max:
                count += 1
            new_max = max(curr_max, node.val)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        return count