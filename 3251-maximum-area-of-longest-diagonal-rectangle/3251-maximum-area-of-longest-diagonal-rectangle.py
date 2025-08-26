from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diag2 = -1
        best_area = 0
        for L, W in dimensions:
            diag2 = L*L + W*W
            area = L*W
            if diag2 > best_diag2 or (diag2 == best_diag2 and area > best_area):
                best_diag2 = diag2
                best_area = area
        return best_area
