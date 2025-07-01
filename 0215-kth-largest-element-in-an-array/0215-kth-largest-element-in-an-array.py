import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_smallest = n - k
        
        left, right = 0, n - 1
        while left <= right:
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            
            lt = left
            gt = right
            i = left + 1
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            
            if k_smallest < lt:
                right = lt - 1
            elif k_smallest > gt:
                left = gt + 1
            else:
                return pivot
        return nums[left]