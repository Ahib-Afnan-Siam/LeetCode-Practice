import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_ptr = 0
        right_ptr = n - 1
        left_heap = []
        right_heap = []
        
        for _ in range(candidates):
            if left_ptr <= right_ptr:
                heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                left_ptr += 1
        
        for _ in range(candidates):
            if left_ptr <= right_ptr:
                heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                right_ptr -= 1
        
        total_cost = 0
        for _ in range(k):
            if not left_heap and not right_heap:
                break
            if not left_heap:
                c, idx = heapq.heappop(right_heap)
                total_cost += c
                if left_ptr <= right_ptr:
                    heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                    right_ptr -= 1
            elif not right_heap:
                c, idx = heapq.heappop(left_heap)
                total_cost += c
                if left_ptr <= right_ptr:
                    heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                    left_ptr += 1
            else:
                if left_heap[0][0] <= right_heap[0][0]:
                    c, idx = heapq.heappop(left_heap)
                    total_cost += c
                    if left_ptr <= right_ptr:
                        heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                        left_ptr += 1
                else:
                    c, idx = heapq.heappop(right_heap)
                    total_cost += c
                    if left_ptr <= right_ptr:
                        heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                        right_ptr -= 1
        
        return total_cost