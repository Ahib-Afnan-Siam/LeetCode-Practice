class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # Helper function to check if subarray is strictly increasing
        def is_increasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        # Iterate through possible starting points for adjacent subarrays
        for a in range(n - 2 * k + 1):
            b = a + k
            if is_increasing(a) and is_increasing(b):
                return True
        
        return False
