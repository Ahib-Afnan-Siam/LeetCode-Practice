import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        low, high = -10**10 - 1, 10**10 + 1
        
        while low < high:
            mid_val = (low + high) // 2
            if self.count_pairs(nums1, nums2, mid_val) < k:
                low = mid_val + 1
            else:
                high = mid_val
        
        return low
    
    def count_pairs(self, nums1, nums2, mid_val):
        count = 0
        for a in nums1:
            if a == 0:
                if mid_val >= 0:
                    count += len(nums2)
            elif a > 0:
                target = mid_val / a
                idx = bisect.bisect_right(nums2, target)
                count += idx
            else:
                target = mid_val / a
                idx = bisect.bisect_left(nums2, target)
                count += (len(nums2) - idx)
        return count