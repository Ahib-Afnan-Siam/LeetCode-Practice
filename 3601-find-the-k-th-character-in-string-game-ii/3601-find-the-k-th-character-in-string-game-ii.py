class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        if n == 0:
            return 'a'
        
        lengths = [1] * (n + 1)
        for i in range(1, n + 1):
            lengths[i] = lengths[i - 1] * 2
        
        offset = 0
        cur = k
        
        for i in range(n - 1, -1, -1):
            half = lengths[i]
            if cur > half:
                cur -= half
                if operations[i] == 1:
                    offset += 1
        
        offset %= 26
        return chr(ord('a') + offset)