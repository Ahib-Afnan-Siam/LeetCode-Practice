class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total_substrings = n * (n + 1) // 2
        zeros = []
        for i, char in enumerate(s):
            if char == '0':
                zeros.append(i)
        m = len(zeros)
        non_dominant = 0
        
        for k in range(1, min(201, m + 1)):
            T = k * k + k - 2
            for i in range(0, m - k + 1):
                start_min = 0 if i == 0 else zeros[i - 1] + 1
                start_max = zeros[i]
                end_min = zeros[i + k - 1]
                end_max = n - 1 if i + k == m else zeros[i + k] - 1
                
                s0 = max(start_min, end_min - T)
                if s0 > start_max:
                    continue
                    
                high1 = min(start_max, end_max - T)
                if s0 <= high1:
                    num1 = high1 - s0 + 1
                    sum_s = (s0 + high1) * num1 // 2
                    non_dominant += num1 * (T - end_min + 1) + sum_s
                    
                low2 = max(s0, end_max - T + 1)
                if low2 <= start_max:
                    num2 = start_max - low2 + 1
                    non_dominant += num2 * (end_max - end_min + 1)
                    
        if m >= 201:
            count_at_most_200 = 0
            zeros_count = 0
            R = 0
            for L in range(n):
                while R < n and zeros_count + (1 if s[R] == '0' else 0) <= 200:
                    zeros_count += (1 if s[R] == '0' else 0)
                    R += 1
                count_at_most_200 += (R - L)
                if s[L] == '0':
                    zeros_count -= 1
            non_dominant += total_substrings - count_at_most_200
            
        return total_substrings - non_dominant