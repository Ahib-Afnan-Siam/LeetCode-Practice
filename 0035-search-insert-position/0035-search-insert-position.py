class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Calculate mid to prevent potential overflow

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1 # Target is in the left half

        # If the loop finishes, the target was not found.
        # 'left' will be the index where the target should be inserted.
        # This is because 'left' always points to the first element
        # that is greater than or equal to the target.
        return left