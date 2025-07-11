import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Step 1: Sort meetings by their start time
        meetings.sort()
        
        # Step 2: Initialize priority queues
        available_rooms = list(range(n))  # All rooms are initially available
        heapq.heapify(available_rooms)

        occupied_rooms = []  # (end_time, room)
        meeting_count = [0] * n  # Count of meetings held in each room

        for start, end in meetings:
            # Free up rooms that have become available by current start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                end_time, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)
            
            duration = end - start

            if available_rooms:
                # Assign the meeting to the lowest-numbered available room
                room = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room))
                meeting_count[room] += 1
            else:
                # Delay the meeting: wait for the earliest ending room
                end_time, room = heapq.heappop(occupied_rooms)
                heapq.heappush(occupied_rooms, (end_time + duration, room))
                meeting_count[room] += 1

        # Step 3: Find the room with the most meetings, break ties by room number
        max_meetings = max(meeting_count)
        for i, count in enumerate(meeting_count):
            if count == max_meetings:
                return i
