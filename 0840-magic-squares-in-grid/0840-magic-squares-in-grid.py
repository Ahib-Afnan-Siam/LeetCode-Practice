from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def is_magic(r, c):
            # Extract 3x3 grid
            nums = [grid[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            
            # Must contain numbers 1 to 9 exactly once
            if sorted(nums) != list(range(1, 10)):
                return False
            
            # Center must be 5
            if grid[r+1][c+1] != 5:
                return False
            
            # Check rows, columns, diagonals
            s = 15
            return (
                sum(grid[r][c:c+3]) == s and
                sum(grid[r+1][c:c+3]) == s and
                sum(grid[r+2][c:c+3]) == s and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == s and
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == s and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == s and
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == s
            )
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        
        return count
