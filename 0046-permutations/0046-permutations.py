class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False
        
        backtrack()
        return result