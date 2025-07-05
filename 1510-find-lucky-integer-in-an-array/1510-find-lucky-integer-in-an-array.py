from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        max_lucky = -1
        for num, count in freq.items():
            if num == count:
                if num > max_lucky:
                    max_lucky = num
        return max_lucky