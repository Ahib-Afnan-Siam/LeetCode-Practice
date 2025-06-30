from itertools import product

class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.words
        indices = [i for i, char in enumerate(word) if char == '.']
        word_list = list(word)
        n = len(indices)
        for combo in product('abcdefghijklmnopqrstuvwxyz', repeat=n):
            for idx, letter in zip(indices, combo):
                word_list[idx] = letter
            candidate = ''.join(word_list)
            if candidate in self.words:
                return True
        return False