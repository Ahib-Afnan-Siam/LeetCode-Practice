class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = [i for i in range(n) if nums[i] == 0]
        count = 0
        for start in zeros:
            for direction in [1, -1]:
                arr = nums.copy()
                pos = start
                d = direction
                while 0 <= pos < n:
                    if arr[pos] > 0:
                        arr[pos] -= 1
                        d = -d
                        pos += d
                    else:
                        next_pos = pos
                        while True:
                            next_pos += d
                            if next_pos < 0 or next_pos >= n:
                                break
                            if arr[next_pos] > 0:
                                break
                        pos = next_pos
                if all(x == 0 for x in arr):
                    count += 1
        return count