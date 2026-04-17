# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return []
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, low, high = q.popleft()
            if not node: continue

            if not (low < node.val < high): return False
            # left child
            q.append((node.left, low, node.val))
            # right child
            q.append((node.right, node.val, high))
        return True    
        