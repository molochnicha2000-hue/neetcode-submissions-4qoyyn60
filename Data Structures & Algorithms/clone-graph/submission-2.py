"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visit = {}
        def dfs(node):
            if node is None:
                return None
            ans = Node(node.val)
            self.visit[node.val] = ans
            for nei in node.neighbors:
                if nei.val in self.visit:
                    ans.neighbors.append(self.visit[nei.val])
                else:
                    ans.neighbors.append(dfs(nei))
            return ans
        return dfs(node)