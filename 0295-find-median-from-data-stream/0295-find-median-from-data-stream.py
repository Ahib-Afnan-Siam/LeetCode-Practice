import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Upper half (min-heap)
        self.max_heap = []  # Lower half (simulated max-heap using min-heap with negatives)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        popped = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -popped)
        if len(self.max_heap) < len(self.min_heap):
            popped_min = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped_min)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0