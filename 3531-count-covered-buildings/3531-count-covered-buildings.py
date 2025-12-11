from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Group buildings by their x-coordinate (rows) and y-coordinate (columns)
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        # Sort the lists for efficient binary search
        for key in rows:
            rows[key].sort()
        for key in cols:
            cols[key].sort()
        
        count = 0
        for x, y in buildings:
            # Check left and right using the row list
            row_list = rows[x]
            row_idx = bisect.bisect_left(row_list, y)
            
            # If this building is the leftmost or rightmost in its row, skip it
            if row_idx == 0 or row_idx == len(row_list) - 1:
                continue
            
            # Check above and below using the column list
            col_list = cols[y]
            col_idx = bisect.bisect_left(col_list, x)
            
            # If this building is the topmost or bottommost in its column, skip it
            if col_idx == 0 or col_idx == len(col_list) - 1:
                continue
            
            # If all conditions are satisfied, the building is covered
            count += 1
        
        return count