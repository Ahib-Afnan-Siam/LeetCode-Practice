class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        n = len(colors)
        
        i = 0
        while i < n:
            j = i
            current_max = neededTime[i]
            current_sum = neededTime[i]
            
            # Find all consecutive balloons of the same color
            while j + 1 < n and colors[j + 1] == colors[i]:
                j += 1
                current_sum += neededTime[j]
                current_max = max(current_max, neededTime[j])
            
            # If we have consecutive balloons (more than 1)
            if j > i:
                # We keep the balloon with maximum removal time
                # Remove all others in this group
                total_time += current_sum - current_max
            
            i = j + 1
        
        return total_time