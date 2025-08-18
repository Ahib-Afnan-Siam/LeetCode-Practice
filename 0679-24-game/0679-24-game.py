from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs(cards)
    
    def dfs(self, nums: List[float]) -> bool:
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 1e-6
        
        for i in range(n):
            for j in range(i + 1, n):
                new_nums = []
                for k in range(n):
                    if k != i and k != j:
                        new_nums.append(nums[k])
                
                a, b = nums[i], nums[j]
                candidates = [
                    a + b,
                    a * b,
                    a - b,
                    b - a
                ]
                if abs(b) > 1e-6:
                    candidates.append(a / b)
                if abs(a) > 1e-6:
                    candidates.append(b / a)
                
                for cand in candidates:
                    if self.dfs(new_nums + [cand]):
                        return True
        return False