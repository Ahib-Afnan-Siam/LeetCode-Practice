class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7           # full weeks
        days = n % 7             # remaining days
        
        # Total for complete weeks:
        # For each week i (starting from 0), the total = 7*(1+i) + (0+1+2+...+6) = 7*(1+i) + 21
        # So sum over i=0..weeks-1 gives: weeks*28 + 7*(weeks*(weeks-1)//2)
        total = weeks * 28 + 7 * (weeks * (weeks - 1) // 2)
        
        # Add remaining days (next week starts from weeks+1)
        for i in range(days):
            total += weeks + 1 + i
        
        return total
