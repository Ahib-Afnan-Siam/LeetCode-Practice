class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        merged = []
        min_len = min(n1, n2)
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
        if n1 > min_len:
            merged.append(word1[min_len:])
        if n2 > min_len:
            merged.append(word2[min_len:])
        return ''.join(merged)