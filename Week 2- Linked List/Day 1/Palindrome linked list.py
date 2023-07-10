# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=head
        lst=[]
        while temp.next and head.next and head.next.next:
            lst.append(temp.val)
            head=head.next.next
            temp=temp.next
        if head.next:
            lst.append(temp.val)
        count=-1
        while temp.next:
            temp=temp.next
            if lst[count]!=temp.val: return False
            count-=1
        return True