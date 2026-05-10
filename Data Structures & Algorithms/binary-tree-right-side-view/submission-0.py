# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(root):
            nonlocal res
            if not root:
                return []
            
            q = collections.deque([root])

            while q:
                if q[-1].val not in res:
                    res.append(q[-1].val)
                for i in range(len(q)):
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        bfs(root)
        return res