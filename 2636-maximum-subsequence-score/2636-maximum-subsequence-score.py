import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        
        heap = []
        current_sum = 0
        best_score = -10**18
        
        for i, (a, b) in enumerate(pairs):
            if i >= k - 1:
                total = current_sum + a
                score = total * b
                if score > best_score:
                    best_score = score
            
            heapq.heappush(heap, a)
            current_sum += a
            
            if len(heap) > k - 1:
                removed = heapq.heappop(heap)
                current_sum -= removed
        
        return best_score