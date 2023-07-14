# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1)
        newHead.next = head
        temp1 = newHead
        
        while temp1.next and temp1.next.next:
            temp2 = ListNode(temp1.next.val)
            temp2.next=temp1.next.next.next
            temp1.next = temp1.next.next
            temp1=temp1.next
            temp1.next=temp2
            temp1=temp1.next
            
        return newHead.next