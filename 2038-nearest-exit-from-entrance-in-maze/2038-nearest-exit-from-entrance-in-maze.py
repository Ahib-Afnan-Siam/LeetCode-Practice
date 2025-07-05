from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        start_row, start_col = entrance
        visited = set([(start_row, start_col)])
        queue = deque()
        queue.append((start_row, start_col, 0))
        
        while queue:
            r, c, steps = queue.popleft()
            
            if (r == 0 or r == m-1 or c == 0 or c == n-1) and steps > 0:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
        
        return -1