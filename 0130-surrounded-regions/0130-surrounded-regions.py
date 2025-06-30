from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'T'
                queue.append((0, j))
            if board[m-1][j] == 'O':
                board[m-1][j] = 'T'
                queue.append((m-1, j))
                
        for i in range(1, m-1):
            if board[i][0] == 'O':
                board[i][0] = 'T'
                queue.append((i, 0))
            if board[i][n-1] == 'O':
                board[i][n-1] = 'T'
                queue.append((i, n-1))
                
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    board[ni][nj] = 'T'
                    queue.append((ni, nj))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'