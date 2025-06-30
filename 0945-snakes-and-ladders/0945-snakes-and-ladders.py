from collections import deque

class Solution:
    def get_coords(self, s, n):
        d = (s - 1) // n
        r = n - 1 - d
        c = (s - 1) % n
        if d % 2 == 1:
            c = n - 1 - c
        return r, c

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        total = n * n
        if total == 1:
            return 0
        
        visited = [False] * (total + 1)
        queue = deque([1])
        visited[1] = True
        moves = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for next_sq in range(curr + 1, min(curr + 7, total + 1)):
                    r, c = self.get_coords(next_sq, n)
                    if board[r][c] != -1:
                        dest = board[r][c]
                    else:
                        dest = next_sq
                    
                    if dest == total:
                        return moves + 1
                    
                    if not visited[dest]:
                        visited[dest] = True
                        queue.append(dest)
            moves += 1
        
        return -1