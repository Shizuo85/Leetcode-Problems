# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while head and head.next:
            temp = temp.next
            head = head.next.next
            if head == temp:
                return True
        return False