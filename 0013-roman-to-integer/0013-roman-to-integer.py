class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        i = 0
        while i < len (s):
            if len(s) == 1:
                num += dict[s[i]]
                i+=1
            elif i + 1 < len(s) and s[i] == "I":
                if s[i+1]=="V":
                    num +=4
                    i+=2
                elif s[i+1]=="X":
                    num += 9
                    i+=2
                else:
                    num += dict[s[i]]
                    i+=1
            elif i + 1 < len(s) and s[i] == "X":
                if s[i+1] == "L":
                    num += 40
                    i+=2
                elif s[i+1] == "C":
                    num += 90
                    i+=2
                else:
                    num += dict[s[i]]
                    i+=1
            elif i + 1 < len(s) and s[i] == "C":
                if s[i+1] == "D":
                    num += 400
                    i+=2
                elif s[i+1] == "M":
                    num += 900
                    i+=2                   
                else:
                    num += dict[s[i]]
                    i+=1
            else:
                num += dict[s[i]]
                i+=1

        return num