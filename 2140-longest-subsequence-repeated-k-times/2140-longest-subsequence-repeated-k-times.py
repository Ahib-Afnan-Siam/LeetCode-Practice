class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            freq[idx] += 1
        
        dp = [[0] * 26 for _ in range(n+1)]
        for c in range(26):
            dp[n][c] = n
        for i in range(n-1, -1, -1):
            for c in range(26):
                if ord(s[i]) == ord('a') + c:
                    dp[i][c] = i
                else:
                    dp[i][c] = dp[i+1][c]
        
        hot = []
        for c in range(26):
            if freq[c] >= k:
                hot.append(chr(ord('a') + c))
        
        if not hot:
            return ""
        
        max_len = min(n // k, 7)
        
        def is_subsequence(candidate, k, dp, n):
            current = 0
            for _ in range(k):
                for char in candidate:
                    c_index = ord(char) - ord('a')
                    if current >= n:
                        return False
                    if dp[current][c_index] < n:
                        current = dp[current][c_index] + 1
                    else:
                        return False
            return True
        
        for L in range(max_len, 0, -1):
            stack = [('', [0]*26)]
            while stack:
                current, counts = stack.pop()
                if len(current) == L:
                    if is_subsequence(current, k, dp, n):
                        return current
                else:
                    extensions = []
                    for c in hot:
                        idx = ord(c) - ord('a')
                        if counts[idx] < freq[idx] // k:
                            extensions.append(c)
                    extensions.sort(reverse=True)
                    for c in extensions[::-1]:
                        new_counts = counts.copy()
                        idx = ord(c) - ord('a')
                        new_counts[idx] += 1
                        new_string = current + c
                        stack.append((new_string, new_counts))
        return ""