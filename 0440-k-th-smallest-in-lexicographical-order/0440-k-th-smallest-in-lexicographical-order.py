class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count_steps(prefix: int) -> int:
            steps = 0
            curr = prefix
            while curr <= n:
                steps += min(n + 1, curr * 10) - curr
                curr *= 10
            return steps
        
        current = 1
        k -= 1  # We start at 1, so subtract 1 to handle the case when k = 1 directly
        
        while k > 0:
            steps = count_steps(current)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        
        return current
