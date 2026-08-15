# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            if node is None:
                return True
            
            if not (left < node.val < right):
                return False
            
            left_sub = dfs(node.left, left, node.val)
            right_sub = dfs(node.right, node.val, right)

            # print(left_sub, right_sub)
            return left_sub & right_sub
        
        r = dfs(root, float('-inf'), float('inf'))
        return r
