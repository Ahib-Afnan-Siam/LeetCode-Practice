class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        dec = [1] * n

        # inc[i] = length of increasing subarray ending at i
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        # dec[i] = length of increasing subarray starting at i
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = dec[i + 1] + 1

        # binary search for maximum k
        left, right = 1, n // 2
        ans = 0
        while left <= right:
            k = (left + right) // 2
            valid = False
            for i in range(n - 2 * k + 1):
                if inc[i + k - 1] >= k and dec[i + k] >= k:
                    valid = True
                    break
            if valid:
                ans = k
                left = k + 1
            else:
                right = k - 1
        return ans
