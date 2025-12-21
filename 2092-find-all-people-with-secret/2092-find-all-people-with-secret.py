from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        # Person 0 and firstPerson know the secret initially
        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True
        
        i = 0
        while i < len(meetings):
            # Get all meetings at current time
            current_time = meetings[i][2]
            
            # Build graph for current time
            graph = defaultdict(list)
            participants = set()
            
            while i < len(meetings) and meetings[i][2] == current_time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                participants.add(x)
                participants.add(y)
                i += 1
            
            # BFS from all people who know the secret in this time frame
            queue = deque([p for p in participants if knows_secret[p]])
            visited = set(queue)
            
            while queue:
                person = queue.popleft()
                for neighbor in graph[person]:
                    if neighbor not in visited:
                        knows_secret[neighbor] = True
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return [i for i in range(n) if knows_secret[i]]