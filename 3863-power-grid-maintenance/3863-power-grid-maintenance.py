from collections import defaultdict
from sortedcontainers import SortedSet

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Step 1: Build DSU for all stations
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)
        
        # Step 2: Group stations by component
        comp_members = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            comp_members[root].append(i)
        
        # Step 3: Initialize SortedSet for each component (all stations online)
        comp_online = {}
        for root, members in comp_members.items():
            comp_online[root] = SortedSet(members)
        
        # Step 4: Track online status
        online = [True] * (c + 1)
        
        res = []
        
        # Step 5: Process queries
        for t, x in queries:
            root = dsu.find(x)
            if t == 1:
                # Query type [1, x]
                if online[x]:
                    res.append(x)
                else:
                    if len(comp_online[root]) == 0:
                        res.append(-1)
                    else:
                        res.append(comp_online[root][0])  # smallest online
            else:
                # Query type [2, x]
                if online[x]:
                    online[x] = False
                    comp_online[root].discard(x)
        
        return res
