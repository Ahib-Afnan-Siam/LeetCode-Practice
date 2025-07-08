from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ascending, height descending for same widths
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract only heights
        heights = [h for _, h in envelopes]

        # Find LIS on heights
        lis = []
        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)
