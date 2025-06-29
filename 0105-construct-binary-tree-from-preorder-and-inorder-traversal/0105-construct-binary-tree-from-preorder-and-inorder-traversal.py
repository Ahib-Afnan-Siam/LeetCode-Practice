class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            in_root_index = inorder_map[root_val]
            left_size = in_root_index - in_start
            
            root.left = build(pre_start + 1, pre_start + left_size, in_start, in_root_index - 1)
            root.right = build(pre_start + left_size + 1, pre_end, in_root_index + 1, in_end)
            return root
        
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
        