from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Gain function: how much the ratio improves by adding one passing student
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # Python's heapq is a min-heap, so store negative gain to simulate max-heap
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign each extra student to the class with the best marginal gain
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute the final average pass ratio
        total_ratio = 0.0
        for _, p, t in heap:
            total_ratio += p / t

        return total_ratio / len(classes)
