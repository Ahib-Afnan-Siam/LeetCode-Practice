class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write_index = 0
        start = 0
        
        for i in range(n + 1):
            if i == n or chars[i] != chars[start]:
                count = i - start
                chars[write_index] = chars[start]
                write_index += 1
                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[write_index] = digit
                        write_index += 1
                start = i
                
        return write_index