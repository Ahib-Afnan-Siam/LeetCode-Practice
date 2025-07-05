class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, current_sum, current):
            if len(current) == k:
                if current_sum == n:
                    res.append(current[:])
                return
            
            for i in range(start, 10):
                count_needed = k - len(current)
                if 9 - i + 1 < count_needed:
                    break
                min_remaining = i * count_needed + (count_needed * (count_needed - 1)) // 2
                if current_sum + min_remaining > n:
                    break
                current.append(i)
                backtrack(i + 1, current_sum + i, current)
                current.pop()
        
        backtrack(1, 0, [])
        return res