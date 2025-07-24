from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # We'll perform a DFS to compute in and out times, and subtree XORs.
        parent = [ -1 ] * n
        xor = [0] * n
        visited = [False] * n
        stack = [(0, True)]
        order = []
        
        # Post-order traversal to compute xor of subtrees
        while stack:
            node, is_first_visit = stack.pop()
            if is_first_visit:
                visited[node] = True
                stack.append((node, False))
                # Push children in reverse order to process them in order
                for neighbor in reversed(adj[node]):
                    if not visited[neighbor] and neighbor != parent[node]:
                        parent[neighbor] = node
                        stack.append((neighbor, True))
            else:
                xor[node] = nums[node]
                for child in adj[node]:
                    if child != parent[node]:
                        xor[node] ^= xor[child]
                order.append(node)
        
        # To check if u is an ancestor of v
        in_time = [0] * n
        out_time = [0] * n
        time = 0
        # Reset visited
        visited = [False] * n
        stack = [(0, True)]
        while stack:
            node, is_first_visit = stack.pop()
            if is_first_visit:
                visited[node] = True
                in_time[node] = time
                time += 1
                stack.append((node, False))
                # Process children in order
                for neighbor in reversed(adj[node]):
                    if not visited[neighbor] and neighbor != parent[node]:
                        stack.append((neighbor, True))
            else:
                out_time[node] = time - 1
        
        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[u] >= out_time[v]
        
        total_xor = xor[0]
        min_score = float('inf')
        
        # Iterate all possible pairs of edges (u1, v1) and (u2, v2) where v1 is child of u1, v2 child of u2
        # So each edge is stored as (parent, child)
        # So first collect all edges in parent-child form
        parent_child_edges = []
        for a, b in edges:
            if parent[b] == a:
                parent_child_edges.append((a, b))
            else:
                parent_child_edges.append((b, a))
        
        m = len(parent_child_edges)
        for i in range(m):
            a1, b1 = parent_child_edges[i]
            for j in range(i + 1, m):
                a2, b2 = parent_child_edges[j]
                # Case 1: b2 is in the subtree of b1 (which implies a2 is a1 or in the subtree)
                if is_ancestor(b1, b2):
                    # Three parts: subtree(b2), subtree(b1) XOR subtree(b2), total_xor XOR subtree(b1)
                    x = xor[b2]
                    y = xor[b1] ^ xor[b2]
                    z = total_xor ^ xor[b1]
                # Case 2: b1 is in the subtree of b2
                elif is_ancestor(b2, b1):
                    x = xor[b1]
                    y = xor[b2] ^ xor[b1]
                    z = total_xor ^ xor[b2]
                else:
                    # The two subtrees are disjoint
                    x = xor[b1]
                    y = xor[b2]
                    z = total_xor ^ x ^ y
                current_max = max(x, y, z)
                current_min = min(x, y, z)
                min_score = min(min_score, current_max - current_min)
        return min_score