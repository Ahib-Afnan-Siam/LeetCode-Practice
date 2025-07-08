import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_to_index = {}
        starts = []
        for i, (start, _) in enumerate(intervals):
            start_to_index[start] = i
            starts.append(start)
        
        starts.sort()
        n = len(starts)
        result = []
        
        for start_i, end_i in intervals:
            pos = bisect.bisect_left(starts, end_i)
            if pos == n:
                result.append(-1)
            else:
                start_val = starts[pos]
                original_index = start_to_index[start_val]
                result.append(original_index)
                
        return result