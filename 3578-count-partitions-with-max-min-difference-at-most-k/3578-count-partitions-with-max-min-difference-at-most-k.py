from typing import List
from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp[i] = number of ways to partition first i elements
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # Segment tree would be better, but for Python we need an O(n) approach
        # We'll use a sliding window with deques to track min and max
        
        # Deques store indices, maintaining:
        # - min_deque: increasing values (min at front)
        # - max_deque: decreasing values (max at front)
        min_deque = deque()
        max_deque = deque()
        
        # Prefix sum of dp for efficient range sum queries
        prefix_sum = [0] * (n + 1)
        prefix_sum[0] = 1
        
        left = 0  # Left boundary of current valid window
        
        for i in range(n):
            # Update deques with current element
            while min_deque and nums[min_deque[-1]] >= nums[i]:
                min_deque.pop()
            min_deque.append(i)
            
            while max_deque and nums[max_deque[-1]] <= nums[i]:
                max_deque.pop()
            max_deque.append(i)
            
            # Shrink window from left until condition is satisfied
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                # Remove left index from deques if present
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1
            
            # Now window [left, i] is valid
            # We can partition at any point from left to i
            # dp[i+1] = sum of dp[j] for j from left to i
            # Using prefix sum: sum(dp[left..i]) = prefix_sum[i] - prefix_sum[left-1] if left > 0
            if left == 0:
                dp[i + 1] = prefix_sum[i] % MOD
            else:
                dp[i + 1] = (prefix_sum[i] - prefix_sum[left - 1]) % MOD
            
            prefix_sum[i + 1] = (prefix_sum[i] + dp[i + 1]) % MOD
        
        return dp[n] % MOD