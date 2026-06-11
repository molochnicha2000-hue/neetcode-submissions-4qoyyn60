class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        N = len(path)
        
        for cur in path.split("/"):
            if cur == "..":
                if stack:
                    stack.pop()
            else:
                if cur and cur != ".":
                    stack.append(cur)
        
        return "/" + "/".join(stack)
        