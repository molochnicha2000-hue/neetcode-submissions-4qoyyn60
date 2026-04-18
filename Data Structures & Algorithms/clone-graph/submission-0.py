"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            curr_node = q.popleft()

            for nei in curr_node.neighbors:
                if nei not in oldToNew: 
                    #curr_node.neighbors.append(nei) 
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curr_node].neighbors.append(oldToNew[nei])
            #seenNodes = set()
        return oldToNew[node]
        
        