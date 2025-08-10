class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Create a set of sorted digit tuples for all powers of two up to 10^9
        powers = {tuple(sorted(str(1 << i))) for i in range(31)}  # 2^0 to 2^30
        
        # Check if sorted digits of n match any power of 2's sorted digits
        return tuple(sorted(str(n))) in powers
