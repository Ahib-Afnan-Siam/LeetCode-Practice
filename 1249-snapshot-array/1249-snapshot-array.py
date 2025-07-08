class SnapshotArray:

    def __init__(self, length: int):
        self.next_snap_id = 0
        self.history = [[(-1, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.next_snap_id:
            self.history[index][-1] = (self.next_snap_id, val)
        else:
            self.history[index].append((self.next_snap_id, val))

    def snap(self) -> int:
        current_id = self.next_snap_id
        self.next_snap_id += 1
        return current_id

    def get(self, index: int, snap_id: int) -> int:
        arr = self.history[index]
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return arr[right][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)