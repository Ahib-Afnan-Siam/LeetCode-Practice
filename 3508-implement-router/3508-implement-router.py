from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # store packets in FIFO order: (source, dest, ts)
        self.packet_set = set()  # to detect duplicates
        self.dest_map = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        
        # check duplicate
        if packet in self.packet_set:
            return False
        
        # if memory full, evict oldest
        if len(self.queue) >= self.memoryLimit:
            old_src, old_dst, old_ts = self.queue.popleft()
            self.packet_set.remove((old_src, old_dst, old_ts))
            # remove timestamp from dest_map[old_dst]
            ts_list = self.dest_map[old_dst]
            idx = bisect_left(ts_list, old_ts)
            if idx < len(ts_list) and ts_list[idx] == old_ts:
                ts_list.pop(idx)
            if not ts_list:  # cleanup if empty
                del self.dest_map[old_dst]
        
        # insert new packet
        self.queue.append(packet)
        self.packet_set.add(packet)
        self.dest_map[destination].append(timestamp)  # timestamps always increasing
        
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        
        src, dst, ts = self.queue.popleft()
        self.packet_set.remove((src, dst, ts))
        
        ts_list = self.dest_map[dst]
        idx = bisect_left(ts_list, ts)
        if idx < len(ts_list) and ts_list[idx] == ts:
            ts_list.pop(idx)
        if not ts_list:
            del self.dest_map[dst]
        
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        ts_list = self.dest_map[destination]
        left = bisect_left(ts_list, startTime)
        right = bisect_right(ts_list, endTime)
        return right - left
