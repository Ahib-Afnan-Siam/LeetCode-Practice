class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % mod
        
        ans = 0
        right = n - 1
        for left in range(n):
            while right >= left and nums[left] + nums[right] > target:
                right -= 1
            if right < left:
                break
            count = right - left
            ans = (ans + power[count]) % mod
        
        return ans