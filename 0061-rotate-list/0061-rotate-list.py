# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        n = k % length
        if n == 0:
            return head
        
        new_tail = head
        for _ in range(length - n - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head