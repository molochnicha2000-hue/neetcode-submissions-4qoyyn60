class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            best = 0
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[r][c] < grid[nr][nc]:
                    best = max(best, dfs(nr, nc) + 1)
            dp[r][c] = best
            return best
        best = 0
        for r in range(m):
            for c in range(n):        
                best = max(best, dfs(r, c) + 1)
        return best