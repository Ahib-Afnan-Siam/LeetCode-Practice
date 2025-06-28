class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_result = 0
        sign = 1
        operand = 0
        
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                operand = operand * 10 + int(c)
            else:
                current_result += sign * operand
                operand = 0
                if c == '+':
                    sign = 1
                elif c == '-':
                    sign = -1
                elif c == '(':
                    stack.append(current_result)
                    stack.append(sign)
                    current_result = 0
                    sign = 1
                elif c == ')':
                    sign_temp = stack.pop()
                    prev_result = stack.pop()
                    current_result = prev_result + sign_temp * current_result
        
        current_result += sign * operand
        return current_result