from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant_queue = deque()
        dire_queue = deque()
        
        for i, char in enumerate(senate):
            if char == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
                
        while radiant_queue and dire_queue:
            r = radiant_queue.popleft()
            d = dire_queue.popleft()
            
            if r < d:
                radiant_queue.append(r + n)
            else:
                dire_queue.append(d + n)
                
        return "Radiant" if radiant_queue else "Dire"