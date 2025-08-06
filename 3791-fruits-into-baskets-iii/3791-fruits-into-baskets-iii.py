import sys
sys.setrecursionlimit(300000)

NEG_INF = -10**18

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        if n == 0:
            return 0
        tree = [NEG_INF] * (4 * n)
        baskets_arr = baskets
        
        def build_tree(node, l, r):
            if l == r:
                tree[node] = baskets_arr[l]
                return
            mid = (l + r) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            build_tree(left_node, l, mid)
            build_tree(right_node, mid+1, r)
            tree[node] = max(tree[left_node], tree[right_node])
        
        build_tree(0, 0, n-1)
        
        unplaced = 0
        
        def query(node, seg_l, seg_r, f):
            if tree[node] < f:
                return -1
            if seg_l == seg_r:
                return seg_l
            mid = (seg_l + seg_r) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if tree[left_node] >= f:
                left_res = query(left_node, seg_l, mid, f)
                if left_res != -1:
                    return left_res
            if tree[right_node] >= f:
                right_res = query(right_node, mid+1, seg_r, f)
                if right_res != -1:
                    return right_res
            return -1
        
        def update(node, seg_l, seg_r, idx, val):
            if seg_l == seg_r:
                tree[node] = val
                return
            mid = (seg_l + seg_r) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if idx <= mid:
                update(left_node, seg_l, mid, idx, val)
            else:
                update(right_node, mid+1, seg_r, idx, val)
            tree[node] = max(tree[left_node], tree[right_node])
        
        for f in fruits:
            idx = query(0, 0, n-1, f)
            if idx == -1:
                unplaced += 1
            else:
                update(0, 0, n-1, idx, NEG_INF)
                
        return unplaced