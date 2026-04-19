# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        com_anc = root.val
        if ((p.val > com_anc and q.val < com_anc) or
            (p.val < com_anc and q.val > com_anc)): return root
        
        LCA = root
        while LCA:
            if p.val > LCA.val and q.val > LCA.val:
                LCA = LCA.right
            elif p.val < LCA.val and q.val < LCA.val:
                LCA = LCA.left
            else:
                return LCA

        