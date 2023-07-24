# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traversal(start, lst):
            if start:
                lst.append(start.val)
                traversal(start.left, lst)
                traversal(start.right, lst)
            else:
                lst.append(None)
            return lst
        return traversal(p, [])==traversal(q, [])