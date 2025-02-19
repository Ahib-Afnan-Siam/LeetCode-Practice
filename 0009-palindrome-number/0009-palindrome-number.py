class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x!=0 and x%10==0):
            return False
        z = x
        y = 0
        while x > 0:
            y = y * 10+ (x%10)

            x = x // 10
        if z == y:
            return True
        else:
            return False
