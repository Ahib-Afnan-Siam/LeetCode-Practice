import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n_val = len(nums) // 3
        left_min = [0] * (2 * n_val)
        heap_left = []
        s_left = 0
        
        for i in range(2 * n_val):
            if i < n_val:
                s_left += nums[i]
                heapq.heappush(heap_left, -nums[i])
            else:
                if nums[i] < -heap_left[0]:
                    removed = -heapq.heappop(heap_left)
                    s_left = s_left - removed + nums[i]
                    heapq.heappush(heap_left, -nums[i])
            left_min[i] = s_left
        
        R = [0] * (3 * n_val)
        heap_right = []
        s_right = 0
        
        for j in range(3 * n_val - 1, -1, -1):
            if j >= 2 * n_val:
                if len(heap_right) < n_val:
                    s_right += nums[j]
                    heapq.heappush(heap_right, nums[j])
            else:
                if len(heap_right) < n_val:
                    s_right += nums[j]
                    heapq.heappush(heap_right, nums[j])
                else:
                    if nums[j] > heap_right[0]:
                        removed = heapq.heappop(heap_right)
                        s_right = s_right - removed + nums[j]
                        heapq.heappush(heap_right, nums[j])
            R[j] = s_right
        
        ans = float('inf')
        for i in range(n_val - 1, 2 * n_val):
            diff = left_min[i] - R[i + 1]
            if diff < ans:
                ans = diff
        return ans