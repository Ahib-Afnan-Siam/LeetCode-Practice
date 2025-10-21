from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        # build coordinate range covered by any interval
        minL = min(nums) - k
        maxR = max(nums) + k

        # shift offset to keep indices non-negative
        offset = -minL if minL < 0 else 0
        size = maxR + offset + 3

        diff = [0] * (size)
        base = [0] * (size)

        # mark intervals and base counts
        for x in nums:
            L = x - k + offset
            R = x + k + offset
            if L < 0: L = 0
            if R + 1 >= size: R = size - 2
            diff[L] += 1
            diff[R + 1] -= 1
            base[x + offset] += 1

        # sweep to compute coverage for each integer t, evaluate candidate
        ans = 1
        curr = 0
        for t in range(size):
            curr += diff[t]
            if curr == 0:
                continue
            b = base[t]
            # candidate frequency for this target t
            cand = curr if curr < b + numOperations else b + numOperations
            if cand > ans:
                ans = cand

        # cannot exceed n
        return min(ans, n)
