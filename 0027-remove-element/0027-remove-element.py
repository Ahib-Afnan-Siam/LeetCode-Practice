class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        keep_index = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[keep_index] = nums[i]  
                keep_index += 1 
        return keep_index