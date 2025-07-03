# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        prev_rev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev_rev
            prev_rev = current
            current = next_node
        
        max_sum = 0
        p1 = head
        p2 = prev_rev
        while p1 and p2:
            current_sum = p1.val + p2.val
            if current_sum > max_sum:
                max_sum = current_sum
            p1 = p1.next
            p2 = p2.next
        
        return max_sum