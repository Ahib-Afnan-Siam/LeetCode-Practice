class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        
        W = [0.0] * maxPts
        W[0] = 1.0
        window_sum = 1.0
        total = 0.0
        
        for i in range(1, n + 1):
            dp_i = window_sum / maxPts
            
            if i < k:
                window_sum += dp_i
            else:
                total += dp_i
            
            if i - maxPts >= 0 and i - maxPts < k:
                window_sum -= W[i % maxPts]
            
            W[i % maxPts] = dp_i
        
        return total