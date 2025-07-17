class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        sign = 1
        if dividend > 0:
            dividend = -dividend
            sign = -sign
        if divisor > 0:
            divisor = -divisor
            sign = -sign
        
        quotient = 0
        while dividend <= divisor:
            temp = divisor
            power = 1
            while temp >= dividend - temp:
                temp += temp
                power += power
            dividend -= temp
            quotient += power
        
        return quotient if sign == 1 else -quotient