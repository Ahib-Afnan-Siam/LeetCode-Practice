class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        total_left = (total + 1) // 2
        
        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = total_left - i
            
            if i < m and j > 0 and nums2[j-1] > nums1[i]:
                low = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                high = i - 1
            else:
                if i == 0:
                    left_max = nums2[j-1]
                elif j == 0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1], nums2[j-1])
                
                if total % 2 == 1:
                    return float(left_max)
                
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])
                
                return (left_max + right_min) / 2.0