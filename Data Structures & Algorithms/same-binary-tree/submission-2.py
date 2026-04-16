# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1:
            p1 = queue1.popleft()
            p2 = queue2.popleft()
            if not p1 and not p2:
                continue
            if not p1 or not p2 or p1.val != p2.val:
                return False

            queue1.append(p1.left)
            queue1.append(p1.right)
            queue2.append(p2.left)
            queue2.append(p2.right)
        return True
            
        