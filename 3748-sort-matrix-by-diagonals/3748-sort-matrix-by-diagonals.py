
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        if n <= 1:
            return grid

        def collect(i: int, j: int) -> List[int]:
            vals = []
            r, c = i, j
            while r < n and c < n:
                vals.append(grid[r][c])
                r += 1
                c += 1
            return vals

        def write_back(i: int, j: int, vals: List[int]) -> None:
            r, c = i, j
            k = 0
            while r < n and c < n:
                grid[r][c] = vals[k]
                r += 1
                c += 1
                k += 1

        # Bottom-left triangle (including main diagonal): starts at (i,0), i=0..n-1
        for i in range(n):
            vals = collect(i, 0)
            vals.sort(reverse=True)  # non-increasing
            write_back(i, 0, vals)

        # Top-right triangle (strictly above main): starts at (0,j), j=1..n-1
        for j in range(1, n):
            vals = collect(0, j)
            vals.sort()  # non-decreasing
            write_back(0, j, vals)

        return grid
