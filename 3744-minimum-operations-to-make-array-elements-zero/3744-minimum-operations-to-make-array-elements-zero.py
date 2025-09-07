from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # precompute powers of 4 covering up to > 1e9
        pow4 = [1]
        while pow4[-1] <= 10**9:
            pow4.append(pow4[-1] * 4)
        # pow4[k] = 4^k, last one > 1e9

        total = 0
        for l, r in queries:
            n = r - l + 1  # counts the "+1" in f(x) for all x in [l..r]
            T = 0          # sum of floor(log_4 x) over x in [l..r]
            # k starts at 1 because k=0 contributes 0 anyway
            for k in range(1, len(pow4) - 0):  # safe upper bound
                lo = max(l, pow4[k])
                hi = min(r, pow4[k] * 4 - 1)   # end of this base-4 block
                if lo <= hi:
                    T += k * (hi - lo + 1)
                # Early break if the block start already exceeds r
                if pow4[k] > r:
                    break
            S = n + T
            total += (S + 1) // 2  # ceil(S/2)
        return total
