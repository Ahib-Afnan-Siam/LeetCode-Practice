class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end point, then by start point in descending order
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        result = 0
        # Track the two largest numbers we've chosen
        first = -1
        second = -1
        
        for start, end in intervals:
            # If current interval is already covered by our two numbers
            if start <= first:
                continue
            # If current interval has one number in common
            elif start <= second:
                result += 1
                first = second
                second = end
            # If current interval has no numbers in common  
            else:
                result += 2
                first = end - 1
                second = end
        
        return result