class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -float('inf')
        
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                count += 1
        
        return count