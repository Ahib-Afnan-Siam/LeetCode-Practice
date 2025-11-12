import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = sum(1 for num in nums if num == 1)
        if count_ones > 0:
            return n - count_ones
        
        overall_gcd = nums[0]
        for i in range(1, n):
            overall_gcd = math.gcd(overall_gcd, nums[i])
        if overall_gcd != 1:
            return -1
        
        min_len = n
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return (min_len - 1) + (n - 1)