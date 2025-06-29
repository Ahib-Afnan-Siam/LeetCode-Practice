class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        
        def helper(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            in_root_index = inorder_map[root_val]
            left_size = in_root_index - in_start
            
            root.left = helper(in_start, in_root_index - 1, post_start, post_start + left_size - 1)
            root.right = helper(in_root_index + 1, in_end, post_start + left_size, post_end - 1)
            return root
        
        return helper(0, n - 1, 0, n - 1)