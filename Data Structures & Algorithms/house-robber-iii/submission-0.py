# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]
            
            leftP = dfs(node.left)
            rightP = dfs(node.right)
            
            withR = node.val + leftP[1] + rightP[1]
            withoutR = max(leftP) + max(rightP)
            return [withR, withoutR]

        res = dfs(root)
        return max(res)