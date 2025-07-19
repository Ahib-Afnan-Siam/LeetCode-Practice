class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n:
                pos = nums[i] - 1
                if nums[i] == nums[pos]:
                    break
                nums[i], nums[pos] = nums[pos], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1