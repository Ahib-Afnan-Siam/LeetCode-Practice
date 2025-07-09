import math
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        D = [0] * (n + 1)
        for i in range(1, n + 1):
            D[i] = D[i - 1] + (endTime[i - 1] - startTime[i - 1])
        D_total = D[n]
        
        segment0_gap = [0] * n
        for i in range(n):
            segment0_gap[i] = startTime[i] - D[i]
        
        prefix_max0 = [0] * n
        if n > 0:
            prefix_max0[0] = segment0_gap[0]
            for i in range(1, n):
                prefix_max0[i] = max(prefix_max0[i - 1], segment0_gap[i])
        
        segment_last_gap = [0] * n
        for i in range(n):
            segment_last_gap[i] = eventTime - endTime[i] - (D_total - D[i + 1])
        
        suffix_max_last = [0] * n
        if n > 0:
            suffix_max_last[n - 1] = segment_last_gap[n - 1]
            for i in range(n - 2, -1, -1):
                suffix_max_last[i] = max(suffix_max_last[i + 1], segment_last_gap[i])
        
        LOG = 0
        if n > 0:
            LOG = math.floor(math.log2(n)) if n > 1 else 0
        st = None
        if n > 0:
            st = [[0] * n for _ in range(LOG + 1)]
            for i in range(n):
                st[0][i] = segment0_gap[i]
            for j in range(1, LOG + 1):
                step = 1 << (j - 1)
                for i in range(n - (1 << j) + 1):
                    st[j][i] = max(st[j - 1][i], st[j - 1][i + step])
        
        def query_sparse(l, r):
            if l > r:
                return -10**18
            length = r - l + 1
            j = math.floor(math.log2(length))
            return max(st[j][l], st[j][r - (1 << j) + 1])
        
        def feasible(L):
            if n == 0:
                return eventTime >= L
            if k >= n:
                return (eventTime - D_total) >= L
            idx0 = min(n - 1, k)
            if prefix_max0[idx0] >= L:
                return True
            low_idx = max(0, n - 1 - k)
            if low_idx < n and suffix_max_last[low_idx] >= L:
                return True
            for i in range(n):
                j_low = i + 1
                j_high = min(n - 1, i + k + 1)
                if j_low > j_high:
                    continue
                M_val = query_sparse(j_low, j_high)
                if M_val >= segment0_gap[i] + L:
                    return True
            return False
        
        low, high = 0, eventTime
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if feasible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans