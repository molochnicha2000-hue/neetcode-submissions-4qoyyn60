class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = {}
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c, last):
            if r >= rows or c >= cols:
                return 0
            
            if (r, c, last) in dp:
                return dp[(r, c, last)]

            best = 0
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] < last:
                    best = max(best, 1 + dfs(nr, nc, grid[nr][nc]))
            dp[(r, c, last)] = best
            return best

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, 1 + dfs(r, c, grid[r][c]))
        return res