from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m = len(mat)
        n = len(mat[0])
        result = []
        total_diagonals = m + n - 1
        
        for s in range(total_diagonals):
            if s % 2 == 0:
                i = min(s, m - 1)
                j = s - i
                while i >= 0 and j < n:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                j = min(s, n - 1)
                i = s - j
                while j >= 0 and i < m:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1
        
        return result