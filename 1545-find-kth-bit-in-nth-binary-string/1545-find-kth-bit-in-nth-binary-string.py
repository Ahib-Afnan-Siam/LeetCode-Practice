class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert = False
        while n > 1:
            mid = 1 << (n - 1)          # 2^(n-1)
            if k == mid:
                return "1" if not invert else "0"
            if k > mid:
                # map to the mirrored position in the first half
                k = (1 << n) - k        # 2^n - k
                invert = not invert
            n -= 1
        # n == 1
        return "0" if not invert else "1"