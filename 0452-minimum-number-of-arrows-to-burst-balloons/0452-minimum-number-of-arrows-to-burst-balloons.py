class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort the balloons based on their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for start, end in points[1:]:
            # If the current balloon starts after the current arrow position, we need a new arrow
            if start > current_end:
                arrows += 1
                current_end = end
        
        return arrows