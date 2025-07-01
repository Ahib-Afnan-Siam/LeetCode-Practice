class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if low < n and nums[low] == target:
            left_index = low
            low2, high2 = left_index, n - 1
            while low2 <= high2:
                mid2 = (low2 + high2) // 2
                if nums[mid2] <= target:
                    low2 = mid2 + 1
                else:
                    high2 = mid2 - 1
            right_index = low2 - 1
            return [left_index, right_index]
        else:
            return [-1, -1]