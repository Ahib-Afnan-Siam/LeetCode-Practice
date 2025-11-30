class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        
        # If the sum is already divisible by p, no need to remove anything
        if remainder == 0:
            return 0
        
        n = len(nums)
        min_length = n  # Initialize with worst case
        
        # Use a dictionary to store the most recent index for each prefix sum mod p
        prefix_mod = {0: -1}  # prefix_sum % p -> index
        current_prefix = 0
        
        for i in range(n):
            current_prefix = (current_prefix + nums[i]) % p
            
            # We're looking for: (current_prefix - target) % p == remainder
            # So: target = (current_prefix - remainder) % p
            target = (current_prefix - remainder) % p
            
            if target in prefix_mod:
                # Found a valid subarray from prefix_mod[target] + 1 to i
                length = i - prefix_mod[target]
                min_length = min(min_length, length)
            
            # Update the most recent index for current prefix mod
            prefix_mod[current_prefix] = i
        
        # If we couldn't find a valid subarray or the only solution is to remove the whole array
        return min_length if min_length < n else -1