# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while True:
            end = prev
            for _ in range(k):
                end = end.next
                if end is None:
                    break
            if end is None:
                break
                
            next_group = end.next
            start = prev.next
            curr = start
            prev_reverse = next_group
            
            for _ in range(k):
                next_temp = curr.next
                curr.next = prev_reverse
                prev_reverse = curr
                curr = next_temp
                
            prev.next = prev_reverse
            prev = start
        
        return dummy.next