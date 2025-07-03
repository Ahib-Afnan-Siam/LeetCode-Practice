from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_dict = defaultdict(int)
        for i in range(n):
            row_dict[tuple(grid[i])] += 1
        
        col_dict = defaultdict(int)
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            col_dict[tuple(col)] += 1
        
        count = 0
        for key in row_dict:
            if key in col_dict:
                count += row_dict[key] * col_dict[key]
                
        return count