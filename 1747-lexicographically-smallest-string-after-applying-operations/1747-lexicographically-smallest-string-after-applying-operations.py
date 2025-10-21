from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        q = deque([s])
        smallest = s

        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr < smallest:
                smallest = curr

            # Operation 1: Add 'a' to all odd indices
            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            add_op = ''.join(arr)

            # Operation 2: Rotate right by 'b'
            rotate_op = curr[-b:] + curr[:-b]

            # Push next states if not visited
            if add_op not in visited:
                q.append(add_op)
            if rotate_op not in visited:
                q.append(rotate_op)

        return smallest
