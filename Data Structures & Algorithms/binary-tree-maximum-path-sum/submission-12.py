# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
inf = float('inf')
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf
        def dfs(node):
            if node is None:
                return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            self.ans = max(self.ans, max(0, l) + max(0, r) + node.val)
            return max(l, r) + node.val
        dfs(root)
        return self.ans