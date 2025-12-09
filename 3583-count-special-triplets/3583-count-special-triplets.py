class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        # Count prefix occurrences
        prefix_counts = {}
        prefix = [0] * n  # prefix[i] = count of values equal to 2*nums[i] before i
        
        for j in range(n):
            target = nums[j] * 2
            prefix[j] = prefix_counts.get(target, 0)
            # Update counts for current position
            prefix_counts[nums[j]] = prefix_counts.get(nums[j], 0) + 1
        
        # Count suffix occurrences
        suffix_counts = {}
        suffix = [0] * n  # suffix[i] = count of values equal to 2*nums[i] after i
        
        for j in range(n-1, -1, -1):
            target = nums[j] * 2
            suffix[j] = suffix_counts.get(target, 0)
            # Update counts for current position
            suffix_counts[nums[j]] = suffix_counts.get(nums[j], 0) + 1
        
        # Calculate total triplets
        result = 0
        for j in range(n):
            result = (result + prefix[j] * suffix[j]) % MOD
        
        return result