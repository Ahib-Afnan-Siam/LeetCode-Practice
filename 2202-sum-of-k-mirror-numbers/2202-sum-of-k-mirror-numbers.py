class Solution:
    def to_base(self, num: int, k: int) -> str:
        if num == 0:
            return "0"
        s = ''
        n_val = num
        while n_val:
            s = str(n_val % k) + s
            n_val //= k
        return s

    def kMirror(self, k: int, n: int) -> int:
        res = []
        d = 1
        while len(res) < n:
            for root in range(10**(d-1), 10**d):
                s_root = str(root)
                palindrome_str = s_root + s_root[:-1][::-1]
                num_val = int(palindrome_str)
                basek_str = self.to_base(num_val, k)
                if basek_str == basek_str[::-1]:
                    res.append(num_val)
                    if len(res) == n:
                        return sum(res)
            for root in range(10**(d-1), 10**d):
                s_root = str(root)
                palindrome_str = s_root + s_root[::-1]
                num_val = int(palindrome_str)
                basek_str = self.to_base(num_val, k)
                if basek_str == basek_str[::-1]:
                    res.append(num_val)
                    if len(res) == n:
                        return sum(res)
            d += 1
        return sum(res)