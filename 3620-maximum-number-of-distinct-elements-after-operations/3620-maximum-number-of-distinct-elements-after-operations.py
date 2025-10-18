class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        used = set()
        current = -float('inf')
        
        for num in nums:
            # we can assign a value in [num - k, num + k]
            # choose the smallest possible value > current to maximize future flexibility
            val = max(num - k, current + 1)
            if val <= num + k:
                used.add(val)
                current = val
                
        return len(used)
