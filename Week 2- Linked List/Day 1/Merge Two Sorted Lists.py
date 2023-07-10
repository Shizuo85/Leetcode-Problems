# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val>list2.val:
            list1, list2 = list2, list1
        temp1=list1
        
        while temp1.next and list2:
            
            if temp1.next.val>=list2.val:
                temp= ListNode(list2.val)
                temp.next=temp1.next
                temp1.next =temp
                
                list2=list2.next
            temp1=temp1.next
        
        if list2:
            temp1.next=list2
            
        return list1