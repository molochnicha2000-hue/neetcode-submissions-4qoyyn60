# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sortedcontainers
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = k
        res = root.val
        def dfs(node):
            nonlocal current, res          
            if not node:
                return

            dfs(node.left)
            if current == 0:
                return
            current -= 1
            if current == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
