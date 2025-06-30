from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        if beginWord == endWord:
            return 1
        
        queue = deque([beginWord])
        steps = 1
        n = len(beginWord)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr[i]:
                            continue
                        new_word = curr[:i] + c + curr[i+1:]
                        if new_word in wordSet:
                            if new_word == endWord:
                                return steps + 1
                            wordSet.remove(new_word)
                            queue.append(new_word)
            steps += 1
        
        return 0