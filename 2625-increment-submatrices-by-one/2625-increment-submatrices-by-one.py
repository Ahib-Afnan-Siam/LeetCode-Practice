class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create a difference matrix with extra row and column for boundaries
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Mark the updates using the difference array technique
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        # Create the result matrix
        mat = [[0] * n for _ in range(n)]
        
        # Compute the prefix sum to get the actual values
        for i in range(n):
            for j in range(n):
                # Add the value from top and left, subtract top-left
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
                
                mat[i][j] = diff[i][j]
        
        return mat