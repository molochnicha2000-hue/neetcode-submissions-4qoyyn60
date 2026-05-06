# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:   
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res) if res else ""
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if not data or vals[0] == "N" or not vals[0] : 
            return None
        i = 1
        root = TreeNode(vals[0]) # must be int
        q = deque([root])
        while q:
            node = q.popleft()

            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            
            i += 1
            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
            #print(q)
        return root
