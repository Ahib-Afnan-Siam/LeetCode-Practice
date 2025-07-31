class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()
        
        for num in arr:
            next_current = set()
            next_current.add(num)
            for val in current:
                next_current.add(val | num)
            current = next_current
            result.update(current)
        
        return len(result)