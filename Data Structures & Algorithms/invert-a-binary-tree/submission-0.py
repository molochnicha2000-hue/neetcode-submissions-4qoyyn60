# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        
        while queue:
            q = queue.popleft()
            leftNode = q.left

            q.left = q.right
            q.right = leftNode
            if q.left: queue.append(q.left)
            if q.right: queue.append(q.right)
            
        return root
    
   

            
            

        