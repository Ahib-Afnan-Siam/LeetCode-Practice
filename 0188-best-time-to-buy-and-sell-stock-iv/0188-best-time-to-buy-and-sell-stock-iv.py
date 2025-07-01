from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # If k is large enough, treat it as unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                profit += max(0, prices[i] - prices[i-1])
            return profit

        # DP table: dp[t][d] = max profit at day d with at most t transactions
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d-1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t-1][d] - prices[d])

        return dp[k][n-1]
