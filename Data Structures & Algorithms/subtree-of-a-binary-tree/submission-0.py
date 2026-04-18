# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or not subRoot: return True
        if not root: return False
        q = deque([root])
        
        while q:
            node = q.popleft()   
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True          
        
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False

    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        


        