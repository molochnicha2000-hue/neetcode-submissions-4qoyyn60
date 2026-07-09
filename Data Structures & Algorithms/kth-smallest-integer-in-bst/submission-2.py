# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sortedcontainers
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sl = sortedcontainers.SortedList()
        k -= 1
        q = collections.deque([root])

        while len(q) > 0:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sl.add(node.val)
        return sl[k]
