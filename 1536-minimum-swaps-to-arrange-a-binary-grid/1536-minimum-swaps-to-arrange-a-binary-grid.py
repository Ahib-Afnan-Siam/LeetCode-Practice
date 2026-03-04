from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Count trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: Try to place correct row at each position
        for i in range(n):
            needed = n - i - 1
            j = i
            
            # Find a row with enough trailing zeros
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1  # Not possible
            
            # Bubble up row j to position i
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps