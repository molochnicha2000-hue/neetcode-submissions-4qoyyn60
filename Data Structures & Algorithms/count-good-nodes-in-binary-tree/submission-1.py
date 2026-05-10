# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        # node is good_node if from path to node weren't bigger val
        def dfs(root, prevVal):
            nonlocal good_nodes
            if not root:
                return

            cur_prevVal = max(prevVal, root.val)
            if root.val >= prevVal:
                good_nodes += 1

            # if wasn't any bigger node.val += 1 good_node
            # maybe we need store prev_val
            dfs(root.left, cur_prevVal)
            dfs(root.right, cur_prevVal)

        dfs(root, float("-inf"))
        return good_nodes
        