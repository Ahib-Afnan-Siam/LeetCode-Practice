MOD = 10**9 + 7

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Generate all possible a_i where a_i = i^x, i is a positive integer, and a_i <= n
        powers = []
        i = 1
        while True:
            power = i ** x
            if power > n:
                break
            powers.append(power)
            i += 1
        
        # Initialize DP array
        dp = [0] * (n + 1)
        dp[0] = 1  # one way to make sum 0: select nothing
        
        for num in powers:
            for j in range(n, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[n] % MOD