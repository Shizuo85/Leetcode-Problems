# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(start, lst):
            if start:
                traversal(start.left, lst)
                lst.append(start.val)
                traversal(start.right, lst)
            return lst
        return traversal(root, [])