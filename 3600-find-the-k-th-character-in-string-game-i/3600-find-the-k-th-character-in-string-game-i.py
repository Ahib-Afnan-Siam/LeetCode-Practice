class Solution:
    def kthCharacter(self, k: int) -> str:
        n = 0
        total = 1
        while total < k:
            n += 1
            total = 1 << n
        
        count = 0
        for i in range(n, 0, -1):
            L = 1 << (i - 1)
            if k > L:
                k -= L
                count += 1
        
        return chr(97 + (count % 26))