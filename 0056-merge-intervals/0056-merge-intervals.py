class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # Step 1: sort by start time
        
        merged = []
        
        for interval in intervals:
            # If merged is empty OR no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap → merge
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged