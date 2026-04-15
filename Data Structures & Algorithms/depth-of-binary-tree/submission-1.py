# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node = root
        q = deque([node])

        level = 0 
        while q:

            for i in range(len(q)):
                lp = q.popleft()

                if lp.right:
                    q.append(lp.right)   
                if lp.left:
                    q.append(lp.left)
        
            level += 1
        return level