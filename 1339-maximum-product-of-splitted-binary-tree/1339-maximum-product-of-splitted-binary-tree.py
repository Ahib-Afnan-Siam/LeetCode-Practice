class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_product = 0
        
        # Step 1: Calculate total sum of the tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        
        # Step 2: DFS to compute subtree sums and maximize product
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            subtree_sum = node.val + left + right
            
            # Try splitting here
            product = subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, product)
            
            return subtree_sum
        
        dfs(root)
        
        return self.max_product % MOD
