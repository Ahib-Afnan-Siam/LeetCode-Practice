from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 = unoccupied & unguarded
        # 1 = guard
        # 2 = wall
        # 3 = guarded cell
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards and walls
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        # Directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # For each guard, propagate in 4 directions until blocked
        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in (1, 2):
                    # Mark as guarded
                    grid[nr][nc] = 3
                    nr += dr
                    nc += dc
        
        # Count unguarded cells (value 0)
        return sum(cell == 0 for row in grid for cell in row)