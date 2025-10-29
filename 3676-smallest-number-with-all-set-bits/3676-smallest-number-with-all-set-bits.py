class Solution:
    def smallestNumber(self, n: int) -> int:
        # Handle edge case where n is 1
        if n == 1:
            return 1
        
        # Get the bit length of n
        bit_length = n.bit_length()
        
        # Check numbers of the form 2^k - 1
        # Start with the same bit length, then try longer ones
        for k in range(bit_length, bit_length + 2):
            candidate = (1 << k) - 1  # 2^k - 1
            if candidate >= n:
                return candidate
        
        return n  # fallback, though mathematically we should always find one