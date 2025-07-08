import random
import bisect
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        # Find the first index where prefix_sum >= target
        index = bisect.bisect_left(self.prefix_sums, target)
        return index

# Example usage:
# obj = Solution([1, 3])
# print(obj.pickIndex())
