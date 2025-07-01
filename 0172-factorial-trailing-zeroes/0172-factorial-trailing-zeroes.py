class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        divisor = 5
        while divisor <= n:
            count += n // divisor
            divisor *= 5
        return count