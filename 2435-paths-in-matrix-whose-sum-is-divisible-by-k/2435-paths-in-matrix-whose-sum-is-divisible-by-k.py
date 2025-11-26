class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # DP table where dp[i][j] is a list of k counts
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Initialize starting cell
        start_remainder = grid[0][0] % k
        dp[0][0][start_remainder] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                current_val = grid[i][j]
                
                # Check paths from top
                if i > 0:
                    for r in range(k):
                        if dp[i-1][j][r] > 0:
                            new_r = (r + current_val) % k
                            dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD
                
                # Check paths from left  
                if j > 0:
                    for r in range(k):
                        if dp[i][j-1][r] > 0:
                            new_r = (r + current_val) % k
                            dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD
        
        return dp[m-1][n-1][0]