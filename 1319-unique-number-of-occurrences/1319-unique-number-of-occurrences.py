from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = defaultdict(int)
        for num in arr:
            freq_map[num] += 1
        
        frequencies = freq_map.values()
        return len(frequencies) == len(set(frequencies))