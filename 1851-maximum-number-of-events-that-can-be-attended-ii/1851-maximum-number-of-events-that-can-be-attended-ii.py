import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [event[1] for event in events]
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            start, end, value = events[i-1]
            pos = bisect.bisect_left(ends, start, 0, i-1)
            prev_index = pos - 1
            
            for j in range(1, k+1):
                skip_val = dp[i-1][j]
                if prev_index == -1:
                    take_val = value
                else:
                    take_val = dp[prev_index+1][j-1] + value
                dp[i][j] = max(skip_val, take_val)
        
        return max(dp[n])