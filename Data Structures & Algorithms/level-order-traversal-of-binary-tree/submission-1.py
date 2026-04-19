# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([root])
        res = []

        while q:
            #node = q.popleft()
            temp_nodes = []
            for i in range(len(q)):
                temp_node = q.popleft()
                temp_nodes.append(temp_node.val)

                if temp_node.left: q.append(temp_node.left)
                if temp_node.right: q.append(temp_node.right)
            res.append(temp_nodes)
        return res