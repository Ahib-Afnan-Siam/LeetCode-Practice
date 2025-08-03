import bisect

class Solution:
    def maxTotalFruits(self, fruits: list, startPos: int, k: int) -> int:
        n = len(fruits)
        if n == 0:
            return 0
        
        positions = [f[0] for f in fruits]
        amounts = [f[1] for f in fruits]
        
        base = 0
        idx_mid = bisect.bisect_left(positions, startPos)
        if idx_mid < n and positions[idx_mid] == startPos:
            base = amounts[idx_mid]
            amounts_adj = amounts.copy()
            amounts_adj[idx_mid] = 0
        else:
            amounts_adj = amounts.copy()
        
        prefix_adj = [0] * (n + 1)
        for i in range(n):
            prefix_adj[i + 1] = prefix_adj[i] + amounts_adj[i]
        
        idx_start = bisect.bisect_right(positions, startPos) - 1
        idx_end = bisect.bisect_left(positions, startPos)
        
        res1 = 0
        if idx_start >= 0:
            total = 0
            l = 0
            for r in range(idx_start + 1):
                total += amounts_adj[r]
                while l <= r and startPos - positions[l] > k:
                    total -= amounts_adj[l]
                    l += 1
                if total > res1:
                    res1 = total
        
        res2 = 0
        if idx_end < n:
            total = 0
            for r in range(idx_end, n):
                if positions[r] - startPos > k:
                    break
                total += amounts_adj[r]
                if total > res2:
                    res2 = total
        
        res3 = 0
        if idx_start >= 0 and idx_end < n:
            positions_right = positions[idx_end:]
            for l in range(idx_start + 1):
                L = positions[l]
                condA = 2 * L - startPos + k
                condB = startPos + k + L
                
                rA = -1
                if positions_right and condA >= positions_right[0]:
                    pos = bisect.bisect_right(positions_right, condA) - 1
                    if pos >= 0:
                        rA = idx_end + pos
                
                rB = -1
                if positions_right:
                    high_bound = condB // 2
                    if high_bound >= positions_right[0]:
                        pos = bisect.bisect_right(positions_right, high_bound) - 1
                        if pos >= 0:
                            rB = idx_end + pos
                
                if rA == -1 and rB == -1:
                    continue
                elif rA == -1:
                    r_val = rB
                elif rB == -1:
                    r_val = rA
                else:
                    r_val = max(rA, rB)
                
                total_span = prefix_adj[r_val + 1] - prefix_adj[l]
                if total_span > res3:
                    res3 = total_span
        
        return base + max(res1, res2, res3)