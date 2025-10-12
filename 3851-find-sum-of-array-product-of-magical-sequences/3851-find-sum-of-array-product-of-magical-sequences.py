class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        L = n + 10
        
        fact = [1] * (m + 1)
        inv_fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % mod
        for i in range(m + 1):
            inv_fact[i] = pow(fact[i], mod - 2, mod)
        
        precomputed = []
        for i in range(n):
            row = []
            for a in range(0, m + 1):
                term = pow(nums[i], a, mod) * inv_fact[a] % mod
                row.append(term)
            precomputed.append(row)
        
        next_dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(m + 1)]
        for c in range(0, m + 1):
            for s in range(0, k + 1):
                for t in range(0, m + 1):
                    if t == m:
                        if c == 0:
                            if s == k:
                                next_dp[c][s][t] = 1
                        else:
                            cnt = bin(c).count('1')
                            if s + cnt == k:
                                next_dp[c][s][t] = 1
        
        for b in range(L - 1, -1, -1):
            current_dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(m + 1)]
            for c in range(0, m + 1):
                for s in range(0, k + 1):
                    for t in range(0, m + 1):
                        if b < n:
                            P_b = precomputed[b]
                            for a in range(0, m - t + 1):
                                total = c + a
                                new_c = total // 2
                                new_s = s + (total % 2)
                                if new_s > k:
                                    continue
                                new_t = t + a
                                if new_t > m:
                                    continue
                                term = P_b[a]
                                current_dp[c][s][t] = (current_dp[c][s][t] + term * next_dp[new_c][new_s][new_t]) % mod
                        else:
                            a = 0
                            total = c + a
                            new_c = total // 2
                            new_s = s + (total % 2)
                            if new_s > k:
                                continue
                            new_t = t
                            current_dp[c][s][t] = (current_dp[c][s][t] + next_dp[new_c][new_s][new_t]) % mod
            next_dp = current_dp
        
        return fact[m] * next_dp[0][0][0] % mod