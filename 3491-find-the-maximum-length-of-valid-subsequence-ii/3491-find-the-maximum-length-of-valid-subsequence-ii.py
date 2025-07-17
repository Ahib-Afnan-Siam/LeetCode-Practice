from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp0 = [[0] * k for _ in range(k)]
        dp1 = [[0] * k for _ in range(k)]
        ans = 1
        
        for num in nums:
            a = num % k
            updates0 = []
            updates1 = []
            
            for y in range(k):
                candidate0 = max(dp0[a][y], 1, dp1[a][y] + 1)
                candidate1 = max(dp1[y][a], 1, dp0[y][a] + 1)
                updates0.append((y, candidate0))
                updates1.append((y, candidate1))
            
            for y, val in updates0:
                dp0[a][y] = val
                if val > ans:
                    ans = val
            
            for y, val in updates1:
                dp1[y][a] = val
                if val > ans:
                    ans = val
        
        return ans