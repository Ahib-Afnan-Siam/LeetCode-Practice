class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        left = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j-1] + 1
                else:
                    left[i][j] = 0
        
        ans = 0
        for i in range(m):
            for j in range(n):
                min_width = float('inf')
                for k in range(i, -1, -1):
                    if left[k][j] == 0:
                        break
                    min_width = min(min_width, left[k][j])
                    ans += min_width
        
        return ans