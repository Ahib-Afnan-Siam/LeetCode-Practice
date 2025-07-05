import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []
        self.in_heap_set = set()

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.in_heap_set.remove(num)
            return num
        else:
            num = self.current
            self.current += 1
            return num

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.in_heap_set:
            heapq.heappush(self.heap, num)
            self.in_heap_set.add(num)