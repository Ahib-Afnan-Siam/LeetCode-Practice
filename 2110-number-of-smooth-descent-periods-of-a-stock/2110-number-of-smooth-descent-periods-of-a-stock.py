from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 1          # first day always counts
        length = 1         # current descent length
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                length = 1
            total += length
        
        return total
