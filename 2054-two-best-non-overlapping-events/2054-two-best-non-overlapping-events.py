import bisect
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]
        
        # Precompute max value from index i to end
        max_value_from = [0] * n
        max_value_from[-1] = events[-1][2]
        for i in range(n - 2, -1, -1):
            max_value_from[i] = max(events[i][2], max_value_from[i + 1])
        
        # Maximum single event value
        ans = max_value_from[0]
        
        # Consider each event as the first event
        for s, e, v in events:
            j = bisect.bisect_right(starts, e)
            if j < n:
                ans = max(ans, v + max_value_from[j])
        
        return ans