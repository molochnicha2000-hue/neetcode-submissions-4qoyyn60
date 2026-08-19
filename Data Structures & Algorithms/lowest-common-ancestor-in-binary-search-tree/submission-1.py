# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, p2: TreeNode) -> TreeNode:
        if root.val > p.val and root.val < p2.val or root.val < p.val and root.val > p2.val:
            return root
        
        r = root
        while r is not None:
            if p.val > r.val and p2.val > r.val:
                r = r.right
            elif p.val < r.val and p2.val < r.val:
                r = r.left
            else:
                return r