class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = strs[0]
        a = strs[0]
        for i in strs:
            b = ""
            for j in range(min(len(a), len(i))):
                if a[j] == i[j]:
                    b = b + i[j]
                else:
                    break
            if len(b) < len(a):
                a = b
            else:
                pass
        return a


                