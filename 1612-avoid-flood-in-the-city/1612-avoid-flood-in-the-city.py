from typing import List
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}              # lake -> last day it rained
        heap = []              # min-heap of (next_rain_day, lake)

        # Precompute next rain day for each lake
        next_rain = {}
        future = {}
        for i in range(n - 1, -1, -1):
            lake = rains[i]
            if lake > 0:
                if lake in future:
                    next_rain[i] = future[lake]
                future[lake] = i

        for i, lake in enumerate(rains):
            if lake > 0:  # Rainy day
                if lake in full:
                    return []  # Flood happens
                full[lake] = i
                if i in next_rain:
                    heapq.heappush(heap, (next_rain[i], lake))
                ans[i] = -1
            else:  # Dry day
                if heap:
                    nxt, lk = heapq.heappop(heap)
                    ans[i] = lk
                    del full[lk]  # dried
                else:
                    ans[i] = 1  # arbitrary (no urgent lake to dry)

        return ans
