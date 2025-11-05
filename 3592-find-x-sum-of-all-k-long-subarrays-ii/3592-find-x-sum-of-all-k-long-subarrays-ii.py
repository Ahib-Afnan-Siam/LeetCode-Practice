from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = Counter()
        res = []

        # Each item in sorted lists: (-freq, -val)
        top = SortedList()
        rest = SortedList()
        x_sum = 0  # running sum of the x-most frequent elements (with counts)

        def add(num):
            nonlocal x_sum
            prev_freq = freq[num]
            freq[num] += 1
            new_freq = freq[num]

            # Remove old entry
            entry_old = (-prev_freq, -num)
            entry_new = (-new_freq, -num)
            if prev_freq > 0:
                if entry_old in top:
                    top.remove(entry_old)
                    x_sum -= prev_freq * num
                else:
                    rest.remove(entry_old)

            # Insert updated entry
            if len(top) < x:
                top.add(entry_new)
                x_sum += new_freq * num
            else:
                # Compare new entry with smallest in top
                if entry_new < top[-1]:  # higher rank (since -freq, -num)
                    # Move one from top -> rest
                    move = top.pop()
                    rest.add(move)
                    f, v = move
                    x_sum -= (-f) * (-v)

                    # Add new element into top
                    top.add(entry_new)
                    x_sum += new_freq * num
                else:
                    rest.add(entry_new)

        def remove(num):
            nonlocal x_sum
            prev_freq = freq[num]
            freq[num] -= 1
            new_freq = freq[num]

            entry_old = (-prev_freq, -num)
            if entry_old in top:
                top.remove(entry_old)
                x_sum -= prev_freq * num
                if new_freq > 0:
                    entry_new = (-new_freq, -num)
                    rest.add(entry_new)
            else:
                rest.remove(entry_old)
                if new_freq > 0:
                    entry_new = (-new_freq, -num)
                    rest.add(entry_new)

            if freq[num] == 0:
                del freq[num]

            # Rebalance: ensure top has x elements
            if len(top) < x and rest:
                move = rest.pop(0)
                top.add(move)
                f, v = move
                x_sum += (-f) * (-v)

        # Initialize first window
        for i in range(k):
            add(nums[i])
        res.append(x_sum)

        # Slide window
        for i in range(k, n):
            remove(nums[i - k])
            add(nums[i])
            res.append(x_sum)

        return res