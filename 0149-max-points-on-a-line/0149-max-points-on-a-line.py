from collections import defaultdict
from typing import List
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            same_point = 1  # Count the base point itself

            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    same_point += 1
                elif dx == 0:
                    # Vertical line
                    slopes[('inf', 0)] += 1
                else:
                    g = gcd(dx, dy)
                    slope = (dy // g, dx // g)
                    
                    # Normalize slope direction
                    if slope[1] < 0:
                        slope = (-slope[0], -slope[1])
                    
                    slopes[slope] += 1

            current_max = max(slopes.values(), default=0)
            max_points = max(max_points, current_max + same_point)

        return max_points
