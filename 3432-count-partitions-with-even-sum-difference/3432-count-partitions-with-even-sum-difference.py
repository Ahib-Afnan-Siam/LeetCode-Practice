from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # If total sum is odd, no partition gives even difference
        if total_sum % 2 == 1:
            return 0
        
        # If total sum is even, all partitions give even difference
        return n - 1