# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True # edgecase

        q = deque([(root, float("-inf"), float("inf"))]) # node.val, low, high
        while q:
            curr_node, low, high = q.popleft()

            if not(low < curr_node.val < high): return False
            # turn left -> append (left child, low is same, high is node.val  
            if curr_node.left: q.append((curr_node.left, low, curr_node.val))
            # the same sit, but 2 changes
            if curr_node.right: q.append((curr_node.right, curr_node.val, high))
        return True
        