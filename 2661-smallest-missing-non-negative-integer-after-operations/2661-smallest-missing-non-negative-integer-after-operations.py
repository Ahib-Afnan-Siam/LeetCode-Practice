class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        
        # Count frequency of each remainder modulo value
        count = Counter((num % value + value) % value for num in nums)
        
        mex = 0
        while True:
            rem = mex % value
            if count[rem] > 0:
                count[rem] -= 1
                mex += 1
            else:
                return mex
