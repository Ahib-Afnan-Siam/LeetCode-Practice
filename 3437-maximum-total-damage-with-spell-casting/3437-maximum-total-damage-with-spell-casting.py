from bisect import bisect_right
from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        unique = sorted(freq.keys())
        total = [v * freq[v] for v in unique]
        n = len(unique)
        
        dp = [0] * n
        
        for i in range(n):
            # Include current damage
            include = total[i]
            # find index of last damage < v[i] - 2
            j = bisect_right(unique, unique[i] - 3) - 1
            if j >= 0:
                include += dp[j]
            # exclude current damage
            exclude = dp[i-1] if i > 0 else 0
            dp[i] = max(include, exclude)
        
        return dp[-1]
