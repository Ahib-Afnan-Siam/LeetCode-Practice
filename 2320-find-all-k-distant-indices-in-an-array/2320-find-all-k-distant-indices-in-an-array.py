class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        marked = [False] * n
        
        for j in range(n):
            if nums[j] == key:
                start = max(0, j - k)
                end = min(n - 1, j + k)
                for i in range(start, end + 1):
                    marked[i] = True
        
        return [i for i in range(n) if marked[i]]