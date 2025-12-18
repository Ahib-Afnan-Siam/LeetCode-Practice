from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half_k = k // 2
        
        # Calculate base profit
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]
        
        # Prefix sums for quick window calculations
        prefix_strategy_profit = [0] * (n + 1)
        prefix_prices = [0] * (n + 1)
        
        for i in range(n):
            prefix_strategy_profit[i + 1] = prefix_strategy_profit[i] + strategy[i] * prices[i]
            prefix_prices[i + 1] = prefix_prices[i] + prices[i]
        
        max_gain = 0  # We can choose not to modify, so minimum gain is 0
        
        # Try all possible windows of length k
        for L in range(n - k + 1):
            R = L + k - 1
            
            # Original profit in window [L, R]
            original_window_profit = prefix_strategy_profit[R + 1] - prefix_strategy_profit[L]
            
            # New profit in window after modification
            # First half becomes 0 (contribute 0)
            # Second half becomes 1 (contribute prices[i])
            new_window_profit = prefix_prices[R + 1] - prefix_prices[L + half_k]
            
            # Gain from modifying this window
            gain = new_window_profit - original_window_profit
            max_gain = max(max_gain, gain)
        
        return base_profit + max_gain