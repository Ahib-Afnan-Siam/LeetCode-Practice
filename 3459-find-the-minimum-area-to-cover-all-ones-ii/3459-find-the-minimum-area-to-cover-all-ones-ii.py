class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ones = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.append((i, j))
                    
        ans = float('inf')
        
        # Case 1: two horizontal cuts
        if m >= 3:
            for i in range(0, m-1):
                for j in range(i+1, m-1):
                    r1_min, r1_max, c1_min, c1_max = m, -1, n, -1
                    r2_min, r2_max, c2_min, c2_max = m, -1, n, -1
                    r3_min, r3_max, c3_min, c3_max = m, -1, n, -1
                    for (r, c) in ones:
                        if r <= i:
                            r1_min = min(r1_min, r)
                            r1_max = max(r1_max, r)
                            c1_min = min(c1_min, c)
                            c1_max = max(c1_max, c)
                        elif r <= j:
                            r2_min = min(r2_min, r)
                            r2_max = max(r2_max, r)
                            c2_min = min(c2_min, c)
                            c2_max = max(c2_max, c)
                        else:
                            r3_min = min(r3_min, r)
                            r3_max = max(r3_max, r)
                            c3_min = min(c3_min, c)
                            c3_max = max(c3_max, c)
                    if r1_min == m or r2_min == m or r3_min == m:
                        continue
                    area1 = (r1_max - r1_min + 1) * (c1_max - c1_min + 1)
                    area2 = (r2_max - r2_min + 1) * (c2_max - c2_min + 1)
                    area3 = (r3_max - r3_min + 1) * (c3_max - c3_min + 1)
                    total = area1 + area2 + area3
                    if total < ans:
                        ans = total
                        
        # Case 2: two vertical cuts
        if n >= 3:
            for i in range(0, n-1):
                for j in range(i+1, n-1):
                    r1_min, r1_max, c1_min, c1_max = m, -1, n, -1
                    r2_min, r2_max, c2_min, c2_max = m, -1, n, -1
                    r3_min, r3_max, c3_min, c3_max = m, -1, n, -1
                    for (r, c) in ones:
                        if c <= i:
                            r1_min = min(r1_min, r)
                            r1_max = max(r1_max, r)
                            c1_min = min(c1_min, c)
                            c1_max = max(c1_max, c)
                        elif c <= j:
                            r2_min = min(r2_min, r)
                            r2_max = max(r2_max, r)
                            c2_min = min(c2_min, c)
                            c2_max = max(c2_max, c)
                        else:
                            r3_min = min(r3_min, r)
                            r3_max = max(r3_max, r)
                            c3_min = min(c3_min, c)
                            c3_max = max(c3_max, c)
                    if c1_min == n or c2_min == n or c3_min == n:
                        continue
                    area1 = (r1_max - r1_min + 1) * (c1_max - c1_min + 1)
                    area2 = (r2_max - r2_min + 1) * (c2_max - c2_min + 1)
                    area3 = (r3_max - r3_min + 1) * (c3_max - c3_min + 1)
                    total = area1 + area2 + area3
                    if total < ans:
                        ans = total
        
        # Case 3: horizontal then vertical on top
        if m >= 2 and n >= 2:
            for i in range(0, m-1):
                for j in range(0, n-1):
                    r1_min, r1_max, c1_min, c1_max = m, -1, n, -1
                    r2_min, r2_max, c2_min, c2_max = m, -1, n, -1
                    r3_min, r3_max, c3_min, c3_max = m, -1, n, -1
                    for (r, c) in ones:
                        if r <= i:
                            if c <= j:
                                r1_min = min(r1_min, r)
                                r1_max = max(r1_max, r)
                                c1_min = min(c1_min, c)
                                c1_max = max(c1_max, c)
                            else:
                                r2_min = min(r2_min, r)
                                r2_max = max(r2_max, r)
                                c2_min = min(c2_min, c)
                                c2_max = max(c2_max, c)
                        else:
                            r3_min = min(r3_min, r)
                            r3_max = max(r3_max, r)
                            c3_min = min(c3_min, c)
                            c3_max = max(c3_max, c)
                    if r1_min == m or r2_min == m or r3_min == m:
                        continue
                    area1 = (r1_max - r1_min + 1) * (c1_max - c1_min + 1)
                    area2 = (r2_max - r2_min + 1) * (c2_max - c2_min + 1)
                    area3 = (r3_max - r3_min + 1) * (c3_max - c3_min + 1)
                    total = area1 + area2 + area3
                    if total < ans:
                        ans = total
        
        # Case 4: horizontal then vertical on bottom
        if m >= 2 and n >= 2:
            for i in range(0, m-1):
                for j in range(0, n-1):
                    r1_min, r1_max, c1_min, c1_max = m, -1, n, -1
                    r2_min, r2_max, c2_min, c2_max = m, -1, n, -1
                    r3_min, r3_max, c3_min, c3_max = m, -1, n, -1
                    for (r, c) in ones:
                        if r <= i:
                            r1_min = min(r1_min, r)
                            r1_max = max(r1_max, r)
                            c1_min = min(c1_min, c)
                            c1_max = max(c1_max, c)
                        else:
                            if c <= j:
                                r2_min = min(r2_min, r)
                                r2_max = max(r2_max, r)
                                c2_min = min(c2_min, c)
                                c2_max = max(c2_max, c)
                            else:
                                r3_min = min(r3_min, r)
                                r3_max = max(r3_max, r)
                                c3_min = min(c3_min, c)
                                c3_max = max(c3_max, c)
                    if r1_min == m or r2_min == m or r3_min == m:
                        continue
                    area1 = (r1_max - r1_min + 1) * (c1_max - c1_min + 1)
                    area2 = (r2_max - r2_min + 1) * (c2_max - c2_min + 1)
                    area3 = (r3_max - r3_min + 1) * (c3_max - c3_min + 1)
                    total = area1 + area2 + area3
                    if total < ans:
                        ans = total
        
        # Case 5: vertical then horizontal on left
        if n >= 2 and m >= 2:
            for i in range(0, n-1):
                for j in range(0, m-1):
                    r1_min, r1_max, c1_min, c1_max = m, -1, n, -1
                    r2_min, r2_max, c2_min, c2_max = m, -1, n, -1
                    r3_min, r3_max, c3_min, c3_max = m, -1, n, -1
                    for (r, c) in ones:
                        if c <= i:
                            if r <= j:
                                r1_min = min(r1_min, r)
                                r1_max = max(r1_max, r)
                                c1_min = min(c1_min, c)
                                c1_max = max(c1_max, c)
                            else:
                                r2_min = min(r2_min, r)
                                r2_max = max(r2_max, r)
                                c2_min = min(c2_min, c)
                                c2_max = max(c2_max, c)
                        else:
                            r3_min = min(r3_min, r)
                            r3_max = max(r3_max, r)
                            c3_min = min(c3_min, c)
                            c3_max = max(c3_max, c)
                    if c1_min == n or c2_min == n or c3_min == n:
                        continue
                    area1 = (r1_max - r1_min + 1) * (c1_max - c1_min + 1)
                    area2 = (r2_max - r2_min + 1) * (c2_max - c2_min + 1)
                    area3 = (r3_max - r3_min + 1) * (c3_max - c3_min + 1)
                    total = area1 + area2 + area3
                    if total < ans:
                        ans = total
        
        # Case 6: vertical then horizontal on right
        if n >= 2 and m >= 2:
            for i in range(0, n-1):
                for j in range(0, m-1):
                    r1_min, r1_max, c1_min, c1_max = m, -1, n, -1
                    r2_min, r2_max, c2_min, c2_max = m, -1, n, -1
                    r3_min, r3_max, c3_min, c3_max = m, -1, n, -1
                    for (r, c) in ones:
                        if c <= i:
                            r1_min = min(r1_min, r)
                            r1_max = max(r1_max, r)
                            c1_min = min(c1_min, c)
                            c1_max = max(c1_max, c)
                        else:
                            if r <= j:
                                r2_min = min(r2_min, r)
                                r2_max = max(r2_max, r)
                                c2_min = min(c2_min, c)
                                c2_max = max(c2_max, c)
                            else:
                                r3_min = min(r3_min, r)
                                r3_max = max(r3_max, r)
                                c3_min = min(c3_min, c)
                                c3_max = max(c3_max, c)
                    if r1_min == m or r2_min == m or r3_min == m:
                        continue
                    area1 = (r1_max - r1_min + 1) * (c1_max - c1_min + 1)
                    area2 = (r2_max - r2_min + 1) * (c2_max - c2_min + 1)
                    area3 = (r3_max - r3_min + 1) * (c3_max - c3_min + 1)
                    total = area1 + area2 + area3
                    if total < ans:
                        ans = total
        
        return ans