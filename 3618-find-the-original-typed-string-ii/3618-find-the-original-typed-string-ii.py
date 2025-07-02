mod = 10**9 + 7

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        runs = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                runs.append(count)
                count = 1
        runs.append(count)
        
        n_runs = len(runs)
        total_ways = 1
        for L in runs:
            total_ways = (total_ways * L) % mod
        
        if k <= n_runs:
            return total_ways
        
        dp = [0] * k
        dp[0] = 1
        
        for L_i in runs:
            P = [0] * k
            P[0] = dp[0]
            for i in range(1, k):
                P[i] = (P[i-1] + dp[i]) % mod
            
            new_dp = [0] * k
            for s in range(1, k):
                low_bound = s - min(L_i, s)
                if low_bound == 0:
                    total_seg = P[s-1]
                else:
                    total_seg = (P[s-1] - P[low_bound-1]) % mod
                new_dp[s] = total_seg % mod
            dp = new_dp
        
        F = sum(dp) % mod
        ans = (total_ways - F) % mod
        return ans