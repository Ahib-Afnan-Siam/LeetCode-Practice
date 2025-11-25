class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Track the best sums for each remainder
        remainders = [0, 0, 0]
        
        for num in nums:
            # Create a copy to avoid overwriting during iteration
            current = remainders.copy()
            
            for r in current:
                new_sum = r + num
                remainder = new_sum % 3
                remainders[remainder] = max(remainders[remainder], new_sum)
        
        return remainders[0]