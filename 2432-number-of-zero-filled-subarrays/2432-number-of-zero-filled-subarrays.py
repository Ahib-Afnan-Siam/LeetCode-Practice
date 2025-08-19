class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_subarrays = 0
        current_zeros = 0
        
        for num in nums:
            if num == 0:
                current_zeros += 1
            else:
                if current_zeros > 0:
                    total_subarrays += current_zeros * (current_zeros + 1) // 2
                    current_zeros = 0
        
        if current_zeros > 0:
            total_subarrays += current_zeros * (current_zeros + 1) // 2
            
        return total_subarrays