from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Calculate initial power for each city using prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        
        power = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power[i] = prefix[right + 1] - prefix[left]
        
        # Binary search for the maximum minimum power
        low = min(power)
        high = max(power) + k  # Upper bound: add all k to the max city
        ans = low
        
        def can_achieve(target):
            # Sliding window to track additional stations
            add = [0] * n
            total_added = 0
            curr_add = 0
            
            for i in range(n):
                # Remove the effect of stations that are no longer in range
                if i - r - 1 >= 0:
                    curr_add -= add[i - r - 1]
                
                # Check if we need to add more stations at current position
                if power[i] + curr_add < target:
                    need = target - (power[i] + curr_add)
                    total_added += need
                    if total_added > k:
                        return False
                    
                    # Add stations at position min(n-1, i + r) to maximize coverage
                    pos = min(n - 1, i + r)
                    add[pos] += need
                    curr_add += need
            
            return True
        
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans