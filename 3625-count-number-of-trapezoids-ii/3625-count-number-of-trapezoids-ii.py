import math
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
            
        # Structure: slope -> { line_identifier -> count_of_segments }
        # slope is represented as a canonical tuple (dy, dx)
        # line_identifier is a constant value distinguishing parallel lines
        lines_by_slope = defaultdict(lambda: defaultdict(int))
        
        # Structure: midpoint -> { slope -> count_of_segments }
        # midpoint is (x1+x2, y1+y2) (doubled to keep as integers)
        midpoints = defaultdict(lambda: defaultdict(int))
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dy = y2 - y1
                dx = x2 - x1
                
                # Normalize slope using GCD to handle collinearity logic correctly
                g = math.gcd(dy, dx)
                dy //= g
                dx //= g
                
                # Ensure canonical representation of slope (e.g., dx always non-negative)
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                slope = (dy, dx)
                
                # Equation of line: dy*X - dx*Y = C
                # C is the unique identifier for the specific infinite line
                intercept = dy * x1 - dx * y1
                lines_by_slope[slope][intercept] += 1
                
                # Calculate Midpoint (doubled)
                mid_x = x1 + x2
                mid_y = y1 + y2
                midpoints[(mid_x, mid_y)][slope] += 1
                
        total_candidates = 0
        
        # 1. Calculate combinations of parallel segments on DIFFERENT lines.
        # This counts standard trapezoids once and parallelograms twice.
        for slope, line_map in lines_by_slope.items():
            counts = list(line_map.values())
            # We want sum of products of all pairs: sum(counts[i] * counts[j]) for i < j
            # Mathematical shortcut: ((sum)^2 - sum(squares)) / 2
            sum_counts = sum(counts)
            sum_sq = sum(c * c for c in counts)
            total_candidates += (sum_counts * sum_counts - sum_sq) // 2
            
        parallelogram_count = 0
        
        # 2. Calculate Parallelograms (Diagonals bisect each other).
        # Two segments sharing a midpoint form a parallelogram unless they are collinear (same slope).
        for mid, slope_map in midpoints.items():
            counts = list(slope_map.values())
            # We need to pick 2 segments with DIFFERENT slopes sharing this midpoint.
            sum_counts = sum(counts)
            sum_sq = sum(c * c for c in counts)
            parallelogram_count += (sum_counts * sum_counts - sum_sq) // 2
            
        # Subtract the extra count of parallelograms
        return total_candidates - parallelogram_count