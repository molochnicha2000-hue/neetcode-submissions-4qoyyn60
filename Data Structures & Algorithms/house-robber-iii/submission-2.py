# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node, can_rob):
            if not node:
                return 0
            
            mx = dfs(node.left, True) + dfs(node.right, True)
            if can_rob:
                current = node.val + dfs(node.left, False) + dfs(node.right, False)
                mx = max(mx, current)

            return mx
        
        res = dfs(root, True)
        return res
