class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        while i < n - 1:
            if bits[i] == 1:
                i += 2  # Skip two bits for two-bit character
            else:
                i += 1  # Skip one bit for one-bit character
        
        return i == n - 1