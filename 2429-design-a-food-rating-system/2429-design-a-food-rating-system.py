from typing import List, Dict, Tuple
import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Current truth for each food
        self.food_info: Dict[str, Tuple[str, int]] = {}
        # For each cuisine, a heap of (-rating, food_name) to get max rating & lexicographically smallest
        self.cuisine_heap: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = (c, r)
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        # Update truth
        self.food_info[food] = (cuisine, newRating)
        # Push new snapshot; stale ones will be skipped during query
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        # Discard stale tops until top reflects current rating
        while heap:
            neg_r, name = heap[0]
            curr_c, curr_r = self.food_info[name]
            if curr_c == cuisine and -neg_r == curr_r:
                return name
            heapq.heappop(heap)  # stale; remove and keep checking
        return ""  # Shouldn't happen given problem guarantees
