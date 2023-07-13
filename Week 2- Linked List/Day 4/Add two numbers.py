# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newL1 = ListNode(-1)
        newL1.next = l1
        temp1 = newL1
        
        
        newL2 = ListNode(-1)
        newL2.next = l2
        temp2 = newL2
        
        carry=0
        
        while temp1.next and temp2.next:
            Sum = temp1.next.val+temp2.next.val+carry
            carry = Sum//10
            Sum = Sum%10
            
            temp3 = ListNode(Sum)
            temp3.next = temp1.next.next
            temp1.next = temp3
            temp1=temp1.next
            
            temp3 = ListNode(Sum)
            temp3.next = temp2.next.next
            temp2.next = temp3
            temp2=temp2.next
        
        if temp2.next:
            temp1.next= temp2.next
       
        while carry:
            if temp1.next:
                Sum = temp1.next.val+carry
                carry = Sum//10
                Sum = Sum%10

                temp3 = ListNode(Sum)
                temp3.next = temp1.next.next
                temp1.next = temp3
                temp1=temp1.next
            else:
                temp3 = ListNode(1)
                temp3.next = None
                temp1.next = temp3
                temp1=temp1.next
                return newL1.next
        return newL1.next
            