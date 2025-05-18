from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
          return 0
        else:
          total = 0
          temp = []
          a= 10000000
          for i in range(len(nums)):
            temp = []
            total = 0
            b = 0
            total += nums[i]
            temp.append(nums[i])
            if total >= target:
              b = len(temp)
              a = min(a,b)
              temp = []
              total = 0
              continue
            else:
              for j in nums[i+1::]:
                total += j
                temp.append(j)
                if total >= target:
                  b = len(temp)
                  break
            if b > 0:
              a = min(a,b)

          return a