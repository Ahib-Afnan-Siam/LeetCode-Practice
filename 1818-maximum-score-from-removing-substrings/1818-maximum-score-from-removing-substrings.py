class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y:
            first_pattern = ('a', 'b')
            first_val = x
            second_pattern = ('b', 'a')
            second_val = y
        else:
            first_pattern = ('b', 'a')
            first_val = y
            second_pattern = ('a', 'b')
            second_val = x
        
        total = 0
        stack1 = []
        for char in s:
            if stack1 and stack1[-1] == first_pattern[0] and char == first_pattern[1]:
                total += first_val
                stack1.pop()
            else:
                stack1.append(char)
        
        stack2 = []
        for char in stack1:
            if stack2 and stack2[-1] == second_pattern[0] and char == second_pattern[1]:
                total += second_val
                stack2.pop()
            else:
                stack2.append(char)
        
        return total