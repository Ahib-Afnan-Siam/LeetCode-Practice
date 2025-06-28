# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left_tail = left_dummy
        right_tail = right_dummy
        
        curr = head
        while curr:
            if curr.val < x:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next
            curr = curr.next
        
        right_tail.next = None
        left_tail.next = right_dummy.next
        
        return left_dummy.next