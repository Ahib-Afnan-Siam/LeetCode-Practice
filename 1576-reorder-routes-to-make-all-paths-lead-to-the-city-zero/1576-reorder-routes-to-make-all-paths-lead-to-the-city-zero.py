from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        
        visited = [False] * n
        queue = deque()
        queue.append(0)
        visited[0] = True
        reversals = 0
        
        while queue:
            node = queue.popleft()
            for neighbor, cost in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    reversals += cost
                    queue.append(neighbor)
        
        return reversals