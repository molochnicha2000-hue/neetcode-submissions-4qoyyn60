class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        rows, cols = len(s1), len(s2)
        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                return i == rows and j == cols
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            
            res = False
            if i < rows and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)

            if not res and j < cols and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            dp[(i, j, k)] = res
            return res

        return dfs(0, 0, 0)