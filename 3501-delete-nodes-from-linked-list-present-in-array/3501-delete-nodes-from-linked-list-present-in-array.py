# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to set for O(1) lookups
        nums_set = set(nums)
        
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Use two pointers: prev and current
        prev = dummy
        current = head
        
        while current:
            if current.val in nums_set:
                # Skip the current node
                prev.next = current.next
            else:
                # Move prev pointer only when we don't remove current node
                prev = current
            
            # Always move current pointer
            current = current.next
        
        return dummy.next