from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        total = 0

        for n in nums:
            found = False
            for d in range(2, int(math.sqrt(n)) + 1):
                if n % d == 0:
                    other = n // d
                    
                    # More than two non-trivial divisors
                    if d == other:
                        break
                    
                    if is_prime(d) and is_prime(other):
                        total += 1 + d + other + n
                    found = True
                    break

        return total
