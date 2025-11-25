class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        # Find first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        # For each character, count unique characters between first and last occurrence
        for char in first_occurrence:
            if first_occurrence[char] < last_occurrence[char] - 1:
                # Get all unique characters between first and last occurrence
                unique_middle = set(s[first_occurrence[char] + 1 : last_occurrence[char]])
                result += len(unique_middle)
        
        return result