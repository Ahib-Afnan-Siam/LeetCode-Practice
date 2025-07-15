class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        if i >= n:
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        start = i
        while i < n and s[i].isdigit():
            i += 1
        
        if start == i:
            return 0
        
        num_str = s[start:i]
        num = int(num_str) * sign
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num