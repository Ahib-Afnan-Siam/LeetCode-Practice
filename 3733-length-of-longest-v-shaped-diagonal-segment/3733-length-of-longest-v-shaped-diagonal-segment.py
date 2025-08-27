from typing import List, Tuple

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # Diagonal directions: 0: NE, 1: SE, 2: SW, 3: NW
        dirs: List[Tuple[int, int]] = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        cw_idx = {0: 1, 1: 2, 2: 3, 3: 0}  # clockwise mapping

        def starts_forward(di: int, dj: int):
            # Heads of forward chains: predecessor (i-di, j-dj) is OOB
            res = []
            for i in range(n):
                for j in range(m):
                    pi, pj = i - di, j - dj
                    if not (0 <= pi < n and 0 <= pj < m):
                        res.append((i, j))
            return res

        def starts_backward(di: int, dj: int):
            # Tails of forward chains: successor (i+di, j+dj) is OOB
            res = []
            for i in range(n):
                for j in range(m):
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < n and 0 <= nj < m):
                        res.append((i, j))
            return res

        # f[d][i][j]: longest straight prefix (1,2,0,...) ending at (i,j) along direction d
        f = [[[0] * m for _ in range(n)] for _ in range(4)]
        # alt2/alt0[d][i][j]: longest (2,0,2,0,...) / (0,2,0,2,...) chain starting at (i,j) along d
        alt2 = [[[0] * m for _ in range(n)] for _ in range(4)]
        alt0 = [[[0] * m for _ in range(n)] for _ in range(4)]

        # Forward DP for straight prefixes
        for d, (di, dj) in enumerate(dirs):
            for si, sj in starts_forward(di, dj):
                i, j = si, sj
                while 0 <= i < n and 0 <= j < m:
                    best = 1 if grid[i][j] == 1 else 0
                    pi, pj = i - di, j - dj
                    if 0 <= pi < n and 0 <= pj < m:
                        prev = f[d][pi][pj]
                        if prev > 0:
                            expected = 2 if (prev % 2 == 1) else 0
                            if grid[i][j] == expected:
                                best = max(best, prev + 1)
                    f[d][i][j] = best
                    i += di
                    j += dj

        # Reverse DP for alternations (2/0 only)
        for d, (di, dj) in enumerate(dirs):
            for si, sj in starts_backward(di, dj):
                i, j = si, sj
                while 0 <= i < n and 0 <= j < m:
                    ni, nj = i + di, j + dj
                    nxt2 = alt2[d][ni][nj] if 0 <= ni < n and 0 <= nj < m else 0
                    nxt0 = alt0[d][ni][nj] if 0 <= ni < n and 0 <= nj < m else 0
                    v = grid[i][j]
                    if v == 2:
                        alt2[d][i][j] = 1 + nxt0
                        alt0[d][i][j] = 0
                    elif v == 0:
                        alt0[d][i][j] = 1 + nxt2
                        alt2[d][i][j] = 0
                    else:
                        alt2[d][i][j] = 0
                        alt0[d][i][j] = 0
                    i -= di
                    j -= dj

        ans = 0
        # Straight-only best
        for d in range(4):
            for i in range(n):
                for j in range(m):
                    ans = max(ans, f[d][i][j])

        # One clockwise turn at pivot (i,j)
        for d, (di, dj) in enumerate(dirs):
            nd = cw_idx[d]
            ndi, ndj = dirs[nd]
            for i in range(n):
                for j in range(m):
                    L = f[d][i][j]
                    if L == 0:
                        continue
                    ni, nj = i + ndi, j + ndj  # first cell after the turn
                    if 0 <= ni < n and 0 <= nj < m:
                        ext = alt2[nd][ni][nj] if (L % 2 == 1) else alt0[nd][ni][nj]
                        ans = max(ans, L + ext)

        return ans
