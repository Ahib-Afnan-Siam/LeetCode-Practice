# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        def split_off(head, step):
            if not head:
                return None
            cur = head
            for _ in range(step - 1):
                if cur.next is None:
                    break
                cur = cur.next
            next_head = cur.next
            cur.next = None
            return next_head
        
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            p1, p2 = l1, l2
            while p1 and p2:
                if p1.val <= p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            cur.next = p1 if p1 else p2
            head = dummy.next
            tail = head
            while tail and tail.next:
                tail = tail.next
            return head, tail
        
        dummy = ListNode(0)
        dummy.next = head
        size = 1
        
        while size < length:
            prev = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = split_off(left, size)
                next_cur = split_off(right, size) if right else None
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
                cur = next_cur
            size *= 2
        
        return dummy.next