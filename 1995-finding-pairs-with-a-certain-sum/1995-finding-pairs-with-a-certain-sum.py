from collections import defaultdict

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = defaultdict(int)
        for num in nums2:
            self.freq[num] += 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq[old_val] -= 1
        new_val = old_val + val
        self.nums2[index] = new_val
        self.freq[new_val] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            complement = tot - num
            count += self.freq.get(complement, 0)
        return count