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

        def build_quad_tree(r_start, c_start, size):
            # Check if all values in the current sub-grid are the same
            first_val = grid[r_start][c_start]
            all_same = True
            for r in range(r_start, r_start + size):
                for c in range(c_start, c_start + size):
                    if grid[r][c] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break

            # If all values are the same, create a leaf node
            if all_same:
                return Node(val=bool(first_val), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            
            # If values are different, create a non-leaf node and recurse for children
            else:
                half_size = size // 2
                top_left = build_quad_tree(r_start, c_start, half_size)
                top_right = build_quad_tree(r_start, c_start + half_size, half_size)
                bottom_left = build_quad_tree(r_start + half_size, c_start, half_size)
                bottom_right = build_quad_tree(r_start + half_size, c_start + half_size, half_size)
                
                # The val for a non-leaf node can be anything; we'll just set it to True (or False, either is accepted)
                return Node(val=True, isLeaf=False, topLeft=top_left, topRight=top_right, bottomLeft=bottom_left, bottomRight=bottom_right)

        return build_quad_tree(0, 0, n)