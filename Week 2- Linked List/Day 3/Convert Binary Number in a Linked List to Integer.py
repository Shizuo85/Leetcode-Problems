# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def depth(linkedList):
            if linkedList:
                x = depth(linkedList.next)
                y = linkedList.val * 2**x[1]
                return [x[0] + y, x[1]+1]
            else:
                return [0, 0]
        return depth(head)[0]