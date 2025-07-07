import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        max_day = max(end for start, end in events)
        event_index = 0
        heap = []
        count = 0
        
        for day in range(1, max_day + 1):
            # Add all events that start on day
            while event_index < len(events) and events[event_index][0] == day:
                heapq.heappush(heap, events[event_index][1])
                event_index += 1
            
            # Remove events that are no longer available
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            # Attend the event with the earliest end day
            if heap:
                heapq.heappop(heap)
                count += 1
        
        return count