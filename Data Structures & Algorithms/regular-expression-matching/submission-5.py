class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        cur = ""
        def dfs(i, j):
            if (i >= len(s) and j >= len(p)):
                return True
 
            if j >= len(p):
                return False
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            match = (i < len(s) and (s[i] == p[j] or p[j] in "."))
            
            if j + 1 < len(p) and p[j + 1] == "*":
                v1 = dfs(i, j + 2)
                v2 = dfs(i + 1, j) if match else False
                dp[(i, j)] = (v1 or v2)
                return v1 or v2
            
            if match:
                v1 = dfs(i + 1, j + 1)
                dp[(i, j)] = v1
                return v1
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)
