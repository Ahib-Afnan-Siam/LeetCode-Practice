import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        n1 = len(nums1)
        n2 = len(nums2)
        heap = []
        result = []
        
        for i in range(min(n1, k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while k > 0 and heap:
            s, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return result