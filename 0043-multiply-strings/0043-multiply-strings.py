class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)
        arr = [0] * (m + n)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                pos = i + j + 1
                arr[pos] += product
        
        carry = 0
        for k in range(len(arr)-1, -1, -1):
            total = arr[k] + carry
            carry = total // 10
            arr[k] = total % 10
        
        idx = 0
        while idx < len(arr) and arr[idx] == 0:
            idx += 1
        
        return ''.join(str(x) for x in arr[idx:]) if idx < len(arr) else "0"