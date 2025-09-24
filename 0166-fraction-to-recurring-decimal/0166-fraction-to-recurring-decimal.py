class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            return sign + str(integer_part)
        
        fractional_parts = []
        remainder_map = {}
        index = 0
        
        while remainder != 0:
            if remainder in remainder_map:
                start_index = remainder_map[remainder]
                non_repeating = ''.join(fractional_parts[:start_index])
                repeating = ''.join(fractional_parts[start_index:])
                return sign + str(integer_part) + '.' + non_repeating + '(' + repeating + ')'
            
            remainder_map[remainder] = index
            index += 1
            
            remainder *= 10
            digit = remainder // denominator
            fractional_parts.append(str(digit))
            remainder %= denominator
        
        return sign + str(integer_part) + '.' + ''.join(fractional_parts)