class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        res = [""]
        
        for digit in digits:
            temp = []
            for s in res:
                for letter in mapping[digit]:
                    temp.append(s + letter)
            res = temp
        
        return res