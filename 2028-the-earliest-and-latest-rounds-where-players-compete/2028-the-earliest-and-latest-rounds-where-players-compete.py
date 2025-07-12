from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        a0 = firstPlayer - 1
        b0 = n - secondPlayer
        c0 = secondPlayer - firstPlayer - 1
        
        @lru_cache(maxsize=None)
        def dfs(a, b, c):
            if a == b:
                return (1, 1)
            m = a + b + c + 2
            segments = []
            segments.extend([0] * a)
            segments.append(1)
            segments.extend([2] * c)
            segments.append(3)
            segments.extend([4] * b)
            mid_index = (m-1)//2 if m % 2 == 1 else -1
            
            base_x = 0
            base_y = 0
            base_z = 0
            A = 0
            B = 0
            C = 0
            
            if mid_index != -1:
                s_mid = segments[mid_index]
                if s_mid == 0:
                    base_x += 1
                elif s_mid == 2:
                    base_y += 1
                elif s_mid == 4:
                    base_z += 1
            
            for i in range(0, m // 2):
                j = m - 1 - i
                s1 = segments[i]
                s2 = segments[j]
                if s1 == 1 or s1 == 3 or s2 == 1 or s2 == 3:
                    continue
                if s1 == s2:
                    if s1 == 0:
                        base_x += 1
                    elif s1 == 2:
                        base_y += 1
                    elif s1 == 4:
                        base_z += 1
                else:
                    if (s1 == 0 and s2 == 4) or (s1 == 4 and s2 == 0):
                        A += 1
                    elif (s1 == 0 and s2 == 2) or (s1 == 2 and s2 == 0):
                        B += 1
                    elif (s1 == 2 and s2 == 4) or (s1 == 4 and s2 == 2):
                        C += 1
            
            next_states = set()
            if A == 0 and B == 0 and C == 0:
                next_states.add((base_x, base_z, base_y))
            else:
                for u in range(0, A + 1):
                    for v in range(0, B + 1):
                        for w in range(0, C + 1):
                            x = base_x + u + v
                            y = base_y + (B - v) + w
                            z = base_z + (A - u) + (C - w)
                            next_states.add((x, z, y))
            
            min_round = float('inf')
            max_round = 0
            for state in next_states:
                a1, b1, c1 = state
                e, l = dfs(a1, b1, c1)
                if e < min_round:
                    min_round = e
                if l > max_round:
                    max_round = l
            return (1 + min_round, 1 + max_round)
        
        earliest, latest = dfs(a0, b0, c0)
        return [earliest, latest]