from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        for i in range(0, n, k):
            chunk = s[i:i+k]
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            res.append(chunk)
        return res
