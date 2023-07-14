# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycles = set()
        while head:
            if head in cycles:
                return head
            else:
                cycles.add(head)
            head=head.next
        return None