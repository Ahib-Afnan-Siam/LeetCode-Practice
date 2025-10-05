from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):  # only flow uphill or equal
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited
        
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
        
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        
        return list(pacific & atlantic)
