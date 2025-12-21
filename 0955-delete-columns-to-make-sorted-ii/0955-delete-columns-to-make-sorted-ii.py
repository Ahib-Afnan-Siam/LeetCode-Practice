from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)  # Number of strings
        m = len(strs[0])  # Length of each string
        
        # Track which consecutive string pairs are already in order
        # is_sorted[i] = True means strs[i] <= strs[i+1] based on columns processed so far
        is_sorted = [False] * (n - 1)
        deletions = 0
        
        # Process each column from left to right
        for col in range(m):
            # Check if we can keep this column
            can_keep = True
            for i in range(n - 1):
                # If this pair is not yet sorted, check current column
                if not is_sorted[i] and strs[i][col] > strs[i + 1][col]:
                    can_keep = False
                    break
            
            if not can_keep:
                # Must delete this column
                deletions += 1
            else:
                # Keep this column, update sorted status
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][col] < strs[i + 1][col]:
                        is_sorted[i] = True
        
        return deletions