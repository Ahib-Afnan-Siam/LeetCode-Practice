class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        pts = points
        ans = 0

        for i in range(n):
            xi, yi = pts[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = pts[j]

                # A is upper-left (allow same row or same column)
                if xi <= xj and yi >= yj:
                    empty = True
                    # check no other point lies inside or on the rectangle border
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = pts[k]
                        if xi <= xk <= xj and yj <= yk <= yi:
                            empty = False
                            break
                    if empty:
                        ans += 1

        return ans
