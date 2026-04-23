# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            leftpath = dfs(root.left)
            rightpath = dfs(root.right)

            TrLeft = max(0, leftpath)
            TrRight = max(0, rightpath)

            res = max(res, root.val + TrLeft + TrRight)
            return root.val + max(TrLeft, TrRight)
        dfs(root)
        return res
        
        