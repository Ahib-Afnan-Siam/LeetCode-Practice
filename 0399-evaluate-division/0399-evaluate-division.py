from collections import deque, defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            queue = deque([(start, 1.0)])
            visited = set([start])
            while queue:
                node, curr = queue.popleft()
                for neighbor, weight in graph[node].items():
                    if neighbor == end:
                        return curr * weight
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr * weight))
            return -1.0
        
        results = []
        for query in queries:
            results.append(bfs(query[0], query[1]))
        return results