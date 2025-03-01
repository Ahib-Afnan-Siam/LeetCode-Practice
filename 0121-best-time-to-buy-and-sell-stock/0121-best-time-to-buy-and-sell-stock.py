class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      minpro =  float('inf')
      maxpro = 0
      for i in range(len(prices)):
        if prices[i] < minpro:
          minpro = prices[i]
        else:
          maxpro = max(maxpro, prices[i] - minpro)
      return maxpro