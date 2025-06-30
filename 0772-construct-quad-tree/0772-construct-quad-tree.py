"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        def build(r, c, size):
            total = grid[r][c]
            same = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != total:
                        same = False
                        break
                if not same:
                    break
            
            if same:
                return Node(bool(total), True, None, None, None, None)
            
            half = size // 2
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return build(0, 0, n)