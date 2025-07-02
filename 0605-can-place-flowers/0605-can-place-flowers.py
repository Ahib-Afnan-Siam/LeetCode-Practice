class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        length = len(flowerbed)
        while i < length and count < n:
            if flowerbed[i] == 1:
                i += 2
            else:
                prev_empty = (i == 0) or (flowerbed[i-1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i+1] == 0)
                if prev_empty and next_empty:
                    count += 1
                    i += 2
                else:
                    i += 1
        return count >= n