class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        # Collect positions of seats
        seats = [i for i, ch in enumerate(corridor) if ch == 'S']
        
        # Invalid cases
        if len(seats) % 2 != 0 or len(seats) == 0:
            return 0
        
        ways = 1
        
        # Process seat pairs
        for i in range(2, len(seats), 2):
            # Number of positions between previous pair and current pair
            gap = seats[i] - seats[i - 1]
            ways = (ways * gap) % MOD
        
        return ways
