class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            n = nums.count(i)
            if n == 1:
                return i
                break
            else:
                pass