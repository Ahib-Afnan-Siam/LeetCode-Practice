from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()  # remove the last element since array shrinks by 1
        return nums[0]
