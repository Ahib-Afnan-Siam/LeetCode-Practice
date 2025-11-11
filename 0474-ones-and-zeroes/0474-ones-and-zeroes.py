class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Create a 2D DP array with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            # Count zeros and ones in current string
            zeros = s.count('0')
            ones = len(s) - zeros
            
            # Update DP table in reverse to avoid reusing same string
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        return dp[m][n]