import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        current_capital = w
        
        for _ in range(k):
            while i < n and projects[i][0] <= current_capital:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            current_capital += -heapq.heappop(max_heap)
        
        return current_capital