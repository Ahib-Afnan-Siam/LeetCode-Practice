from typing import List, Dict, Tuple
import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        # Map: taskId -> (userId, priority)
        self.task: Dict[int, Tuple[int, int]] = {}
        # Max-heap implemented as min-heap with negated keys.
        # Entries are (-priority, -taskId, taskId)
        self.heap: List[Tuple[int, int, int]] = []
        for userId, taskId, priority in tasks:
            self.task[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task[taskId]
        # Update current record and push a fresh heap entry.
        self.task[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        # Lazy delete: remove from dict; heap entries become stale.
        if taskId in self.task:
            del self.task[taskId]

    def execTop(self) -> int:
        # Pop until we find a live, up-to-date entry.
        while self.heap:
            neg_pri, neg_tid, taskId = heapq.heappop(self.heap)
            if taskId not in self.task:
                continue  # stale (removed)
            userId, curPri = self.task[taskId]
            # Validate that the heap entry matches current priority
            if -neg_pri == curPri and -neg_tid == taskId:
                # Execute: remove from system and return userId
                del self.task[taskId]
                return userId
            # Otherwise stale (edited); keep popping
        return -1
