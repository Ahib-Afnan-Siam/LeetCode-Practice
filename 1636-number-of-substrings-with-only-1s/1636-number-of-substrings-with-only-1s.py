class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        current_length = 0
        
        for char in s:
            if char == '1':
                current_length += 1
            else:
                total = (total + current_length * (current_length + 1) // 2) % MOD
                current_length = 0
        
        total = (total + current_length * (current_length + 1) // 2) % MOD
        return total