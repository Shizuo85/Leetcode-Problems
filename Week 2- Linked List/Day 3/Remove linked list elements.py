# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        temp = dummyHead
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp=temp.next
        return dummyHead.next
    
    