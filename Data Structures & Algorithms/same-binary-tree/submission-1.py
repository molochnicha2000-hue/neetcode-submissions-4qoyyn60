# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([(p, q)])
        while q:
            p1, q1 = q.popleft()
            if not p1 and not q1:
                continue
            if not p1 or not q1 or p1.val != q1.val:
                return False
            q.append((p1.right, q1.right))
            q.append((p1.left, q1.left))
        return True
            
        