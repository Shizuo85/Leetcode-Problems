# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        newHead1 = ListNode(-1)
        newHead2 = ListNode(-1)
        newHead1.next = head
        temp1 = newHead1
        temp2 = newHead2
        
        while head:
            if head.val<x:
                temp1.next = ListNode(head.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(head.val)
                temp2 = temp2.next
            head = head.next
        
        temp1.next = newHead2.next
        return newHead1.next