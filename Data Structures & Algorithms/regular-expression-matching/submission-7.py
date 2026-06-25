class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        P = len(p)
        dp = {}
        def dfs(i, j):
            if i >= N and j >= P:    
                return True

            if j >= P:
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            temp = False
            if j + 1 < P and p[j + 1] == "*":
                v1 = dfs(i, j + 2)
                v2 = dfs(i + 1, j) if (i < len(s) and (s[i] == p[j] or p[j] in ".")) else False
                temp = v1 | v2

            elif (i < len(s) and (s[i] == p[j] or p[j] in ".")):
                temp = dfs(i + 1, j + 1)
            dp[(i, j)] = temp
            return temp
            
        
        res = dfs(0, 0)
        return res