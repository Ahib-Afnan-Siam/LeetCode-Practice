class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        num = 0
        base = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                ans += 1
                if base <= k:
                    base *= 2
            else:
                if base > k:
                    continue
                if num + base > k:
                    continue
                num += base
                ans += 1
                base *= 2
        return ans