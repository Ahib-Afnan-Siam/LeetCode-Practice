class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last < k + 1:
                    return False
                last = i
        return True