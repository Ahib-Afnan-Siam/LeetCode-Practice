from typing import List

MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        first = complexity[0]
        # Check if the first computer has the strictly smallest complexity
        for i in range(1, n):
            if complexity[i] <= first:
                return 0
        
        # All other computers can be unlocked in any order after computer 0
        ans = 1
        for i in range(1, n):
            ans = (ans * i) % MOD
        return ans