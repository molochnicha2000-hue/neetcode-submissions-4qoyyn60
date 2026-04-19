# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #if k == 1 and not root.left: return root.val

        res = []
        stack = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            res.append(node.val)

            #if len(res) == k:
                #break

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        
        res.sort()
        print(res)
        return res[k - 1]
            
