class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            best = 0
            best += + dfs(r + 1, c)
            best += + dfs(r, c + 1)
            dp[(r, c)] = best
            return best
        
        res = dfs(0, 0)
        #print(dp)
        return res