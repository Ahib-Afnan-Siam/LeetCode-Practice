class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)  # dp[d] = new learners on day d (1-indexed)
        dp[1] = 1
        can_share = 0  # number of people who can share today

        for d in range(2, n + 1):
            # People who start sharing today
            if d - delay >= 1:
                can_share = (can_share + dp[d - delay]) % MOD
            # People who forgot today (cannot share anymore)
            if d - forget >= 1:
                can_share = (can_share - dp[d - forget]) % MOD
            dp[d] = can_share

        # Sum of those who still remember at end of day n:
        # they learned on days max(1, n - forget + 1) .. n
        start = max(1, n - forget + 1)
        return sum(dp[start:n + 1]) % MOD
