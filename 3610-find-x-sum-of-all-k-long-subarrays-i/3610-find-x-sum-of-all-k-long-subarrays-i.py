from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            
            # Sort by frequency first (descending), then by value (descending)
            top_x = sorted(freq.items(), key=lambda item: (item[1], item[0]), reverse=True)[:x]
            
            # Get the elements that are in the top x frequencies
            keep = set([num for num, _ in top_x])
            
            # Calculate the sum of elements that belong to the top x frequent numbers
            total = sum(num for num in window if num in keep)
            res.append(total)
        
        return res
