from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Transpose the grid to get columns as rows
        # Then check if each "column" (now a row) is sorted
        deletions = 0
        
        # For each column index
        for col in zip(*strs):  # zip(*strs) gives us tuples of column values
            # Check if the column is sorted
            if list(col) != sorted(col):
                deletions += 1
                
        return deletions