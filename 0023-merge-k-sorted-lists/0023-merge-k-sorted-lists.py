import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, id(head), head))
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                next_node = node.next
                heapq.heappush(heap, (next_node.val, id(next_node), next_node))
        return dummy.next