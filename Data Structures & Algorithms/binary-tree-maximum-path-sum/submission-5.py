# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            posL = max(0, l)
            posR = max(0, r)

            res = max(res, node.val + posL + posR)
            return node.val + max(posL, posR)
        dfs(root)
        return res 