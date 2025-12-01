class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total_power = sum(batteries)
        
        left, right = 0, total_power // n
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if we can run all computers for 'mid' minutes
            total_available = 0
            for battery in batteries:
                total_available += min(battery, mid)
            
            if total_available >= n * mid:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result