class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max = max_so_far = nums[0]
        cur_min = min_so_far = nums[0]
        
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_so_far = max(max_so_far, cur_max)
            cur_min = min(nums[i], cur_min + nums[i])
            min_so_far = min(min_so_far, cur_min)
        
        if max_so_far < 0:
            return max_so_far
        return max(max_so_far, total - min_so_far)