from typing import List
import heapq

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        
        # (time_user_comes_back, user_id)
        comeback_heap = []
        
        # OFFLINE must be processed before MESSAGE at same timestamp
        def event_priority(e):
            return 0 if e[0] == "OFFLINE" else 1
        
        events.sort(key=lambda e: (int(e[1]), event_priority(e)))
        
        def process_comebacks(current_time):
            while comeback_heap and comeback_heap[0][0] <= current_time:
                _, uid = heapq.heappop(comeback_heap)
                online[uid] = True
        
        for event_type, ts_str, value in events:
            timestamp = int(ts_str)
            
            # Process users coming back online first
            process_comebacks(timestamp)
            
            if event_type == "OFFLINE":
                uid = int(value)
                online[uid] = False
                heapq.heappush(comeback_heap, (timestamp + 60, uid))
            
            else:  # MESSAGE
                if value == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                        
                elif value == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                            
                else:
                    for token in value.split():
                        uid = int(token[2:])
                        mentions[uid] += 1
        
        return mentions