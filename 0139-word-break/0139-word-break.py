class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(word) for word in word_set) if word_set else 0
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            start_index = max(0, i - max_len)
            for j in range(start_index, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]