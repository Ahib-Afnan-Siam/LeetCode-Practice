class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if s[0] == i:
                s = s[1::]
            else:
                pass
        if s == "":
            return True
        else:
            return False

        