# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        q = root
        n = 0
        while q or stack:
            while q:
                stack.append(q)
                q = q.left
            q = stack.pop()
            n += 1
            if n == k: return q.val

            q = q.right
        