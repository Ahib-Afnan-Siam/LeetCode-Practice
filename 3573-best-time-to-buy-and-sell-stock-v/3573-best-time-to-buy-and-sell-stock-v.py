from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # Initialize DP arrays
        dp = [[0] * n for _ in range(k + 1)]
        
        for t in range(1, k + 1):
            # best_normal and best_short track the best values for starting a new transaction
            best_normal = float('-inf')
            best_short = float('-inf')
            
            for i in range(1, n):
                # Update best values using the previous day's price
                # We can start a transaction at day i-1
                best_normal = max(best_normal, (dp[t-1][i-2] if i >= 2 else 0) - prices[i-1])
                best_short = max(best_short, (dp[t-1][i-2] if i >= 2 else 0) + prices[i-1])
                
                # No transaction ending at day i
                dp[t][i] = dp[t][i-1]
                
                # Normal transaction: buy at some j < i, sell at i
                dp[t][i] = max(dp[t][i], best_normal + prices[i])
                
                # Short transaction: sell at some j < i, buy back at i
                dp[t][i] = max(dp[t][i], best_short - prices[i])
        
        return dp[k][-1]