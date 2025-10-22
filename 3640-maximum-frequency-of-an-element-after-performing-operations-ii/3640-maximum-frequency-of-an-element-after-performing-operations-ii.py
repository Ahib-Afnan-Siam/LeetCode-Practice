from typing import List
from collections import defaultdict, Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        counts = Counter(nums)

        # Build events: +1 at L, -1 at R+1 so coverage counts integer points [L..R] inclusive
        events = defaultdict(int)
        for v in nums:
            L = v - k
            R = v + k
            events[L] += 1
            events[R + 1] -= 1

        # Points to sweep: all event keys and all distinct nums (we need cover at nums values)
        points = sorted(set(events.keys()) | set(counts.keys()))

        cur_cover = 0
        ans = 1  # at least one element
        # Sweep in increasing order; when at point p, apply events[p] first (adds/subtracts)
        for p in points:
            cur_cover += events.get(p, 0)

            # case 1: choose x = p (may be a nums value)
            if p in counts:
                # elements already equal to p: counts[p]
                # can add up to numOperations other indices (but limited by cur_cover)
                candidate = min(cur_cover, counts[p] + numOperations)
                if candidate > ans:
                    ans = candidate

            # case 2: choose x = p even if not in counts (count[x] == 0)
            # then best we can do is min(cur_cover, numOperations)
            # (this handles non-existing integer targets)
            candidate_no_equal = min(cur_cover, numOperations)
            if candidate_no_equal > ans:
                ans = candidate_no_equal

        return ans
