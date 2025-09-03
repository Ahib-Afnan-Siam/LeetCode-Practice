from typing import List
import bisect

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x asc, y desc so for same x the potential Alice (higher y) comes before Bob
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            xi, yi = points[i]
            S = []  # sorted list of y's for points (i, k) with i < k < j
            for j in range(i + 1, n):
                xj, yj = points[j]
                if yj > yi:
                    # Bob must be at or below Alice
                    # (xj >= xi is guaranteed by the sort)
                    pass
                else:
                    # Check if there exists any y in S within [yj, yi]
                    left = bisect.bisect_left(S, yj)
                    right = bisect.bisect_right(S, yi)
                    if left == right:
                        ans += 1
                # Insert current yj into S for future j's
                bisect.insort(S, yj)

        return ans
