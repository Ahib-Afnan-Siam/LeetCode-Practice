from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[i] = length of longest valid sequence ending at column i
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if we can extend the sequence ending at j with column i
                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The maximum number of columns we can keep
        max_keep = max(dp)
        
        # Minimum deletions = total columns - columns we can keep
        return m - max_keep