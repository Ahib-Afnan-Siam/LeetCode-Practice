from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b  # avoid overflow order

        stack: List[int] = []
        for x in nums:
            cur = x
            # Keep merging with the stack top while they are non-coprime
            while stack:
                g = gcd(stack[-1], cur)
                if g == 1:
                    break
                cur = lcm(stack.pop(), cur)
            stack.append(cur)
        return stack
