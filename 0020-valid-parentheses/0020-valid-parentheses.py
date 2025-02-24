class Solution:
    def isValid(self, s: str) -> bool:
        al = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                al.append(s[i])
            elif s[i] == ')':
                if al and al[-1] == '(':
                    al.pop()
                else:
                    return False
            elif s[i] == '}':
                if al and al[-1] == '{':
                    al.pop()
                else:
                    return False
            elif s[i] == ']':
                if al and al[-1] == '[':
                    al.pop()
                else:
                    return False
        return len(al) == 0
