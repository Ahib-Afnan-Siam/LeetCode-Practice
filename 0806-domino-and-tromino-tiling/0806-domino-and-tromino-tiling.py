class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n <= 1:
            return 1
        a, b, inc = 1, 1, 0
        for i in range(2, n + 1):
            new_b = (b + a + 2 * inc) % mod
            new_inc = (inc + a) % mod
            a, b, inc = b, new_b, new_inc
        return b % mod