class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Continue until we have exactly 2 digits
        while len(s) > 2:
            new_s = []
            # For each pair of consecutive digits
            for i in range(len(s) - 1):
                # Calculate sum modulo 10
                total = int(s[i]) + int(s[i + 1])
                new_digit = total % 10
                new_s.append(str(new_digit))
            # Replace s with the new sequence
            s = ''.join(new_s)
        
        # Check if the final two digits are the same
        return s[0] == s[1]