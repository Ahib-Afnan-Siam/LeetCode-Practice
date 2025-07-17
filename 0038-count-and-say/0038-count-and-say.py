class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        current = "1"
        for _ in range(2, n + 1):
            next_str = []
            i = 0
            while i < len(current):
                count = 1
                j = i + 1
                while j < len(current) and current[j] == current[i]:
                    count += 1
                    j += 1
                next_str.append(str(count) + current[i])
                i = j
            current = ''.join(next_str)
        return current