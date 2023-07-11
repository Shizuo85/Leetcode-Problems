# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        temp = head
        if left ==1:
            leftList = None
        else:
            leftList = ListNode(head.val)
            leftList.next = None
        cur = leftList
        count= 1
        while temp:
            if left == count:
                newHead = ListNode(temp.val)
                temp1=newHead
                rightList = temp.next
                
                while count<right:
                    temp1.next = ListNode(rightList.val)
                    rightList=rightList.next
                    temp1 = temp1.next
                    count+=1
                
                temp2 = newHead
                prev = None
                while temp2:
                    temp2.next, prev = prev, temp2.next
                    temp2, prev = prev, temp2
                
                if cur:
                    cur.next = prev
                else:
                    leftList, cur = prev, prev
                while cur.next:
                    cur=cur.next
                cur.next=rightList
                break
                
            temp = temp.next
            if temp and left-count!=1:
                cur.next = ListNode(temp.val)
                cur = cur.next
            count+=1
        return leftList
                    