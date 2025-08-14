class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        n = len(num)
        for i in range(n - 2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i] == '9':
                    return "999"
                candidate = num[i:i+3]
                if candidate > best:
                    best = candidate
        return best