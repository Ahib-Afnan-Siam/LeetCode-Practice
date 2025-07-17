class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = board[i][j]
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[i//3][j//3].add(d)
        
        def backtrack(index):
            if index == 81:
                return True
            r = index // 9
            c = index % 9
            if board[r][c] != '.':
                return backtrack(index + 1)
            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[r//3][c//3]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[r//3][c//3].add(d)
                    if backtrack(index + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[r//3][c//3].remove(d)
            return False
        
        backtrack(0)