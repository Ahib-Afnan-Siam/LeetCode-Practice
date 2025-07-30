class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_len = 0
        cur_len = 0
        for num in nums:
            if num == max_val:
                cur_len += 1
            else:
                cur_len = 0
            if cur_len > max_len:
                max_len = cur_len
        return max_len