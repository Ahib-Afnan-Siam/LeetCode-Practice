class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        even_alt = 0
        odd_alt = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
                even_alt = odd_alt + 1
            else:
                count_odd += 1
                odd_alt = even_alt + 1
        return max(count_even, count_odd, even_alt, odd_alt)