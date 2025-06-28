# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.next and curr.next.val == curr.val:
                temp = curr
                while temp.next and temp.next.val == curr.val:
                    temp = temp.next
                prev.next = temp.next
                curr = temp.next
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next