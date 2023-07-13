# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            temp=temp.next
            l+=1
        if l<2 or k%l==0:
            return head
        k = k%l
        
        newHead = ListNode(-1)
        temp2 = newHead
        temp = head
        count = 0
        
        while count<l-k:
            count+=1
            temp2.next = ListNode(temp.val)
            temp = temp.next
            temp2 = temp2.next
        
        temp2 = temp
        
        while temp2.next:
            temp2 = temp2.next
        temp2.next = newHead.next
        
        return temp
            