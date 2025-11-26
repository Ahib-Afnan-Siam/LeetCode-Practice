class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0  # Start with right direction
        
        row, col = 0, 0
        num = 1
        
        while num <= n * n:
            matrix[row][col] = num
            num += 1
            
            # Calculate next position
            next_row = row + directions[dir_index][0]
            next_col = col + directions[dir_index][1]
            
            # If next position is out of bounds or already filled, change direction
            if (next_row < 0 or next_row >= n or 
                next_col < 0 or next_col >= n or 
                matrix[next_row][next_col] != 0):
                dir_index = (dir_index + 1) % 4
                next_row = row + directions[dir_index][0]
                next_col = col + directions[dir_index][1]
            
            row, col = next_row, next_col
        
        return matrix