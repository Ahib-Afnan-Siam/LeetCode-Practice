from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq = Counter(s)

        # Maximum vowel frequency (0 if no vowels exist)
        max_vowel = max((count for ch, count in freq.items() if ch in vowels), default=0)

        # Maximum consonant frequency (0 if no consonants exist)
        max_consonant = max((count for ch, count in freq.items() if ch not in vowels), default=0)

        return max_vowel + max_consonant
