class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.strip()
        l = temp.split()
        n = len(l[-1])
        return n