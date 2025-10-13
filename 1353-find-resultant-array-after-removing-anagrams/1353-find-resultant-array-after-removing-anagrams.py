class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = ""
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word != prev:
                res.append(word)
                prev = sorted_word
        return res
