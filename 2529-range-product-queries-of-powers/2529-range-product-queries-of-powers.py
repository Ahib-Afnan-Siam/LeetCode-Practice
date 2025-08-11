MOD = 10**9 + 7

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        max_total_exp = 500
        pow2 = [1] * (max_total_exp + 1)
        for exp in range(1, max_total_exp + 1):
            pow2[exp] = (pow2[exp - 1] * 2) % MOD
        
        exp_arr = []
        temp = n
        bit_index = 0
        while temp:
            if temp & 1:
                exp_arr.append(bit_index)
            temp >>= 1
            bit_index += 1
        
        m = len(exp_arr)
        prefix_exp = [0] * (m + 1)
        for i in range(1, m + 1):
            prefix_exp[i] = prefix_exp[i - 1] + exp_arr[i - 1]
        
        ans = []
        for l, r in queries:
            total_exp = prefix_exp[r + 1] - prefix_exp[l]
            ans.append(pow2[total_exp])
        
        return ans