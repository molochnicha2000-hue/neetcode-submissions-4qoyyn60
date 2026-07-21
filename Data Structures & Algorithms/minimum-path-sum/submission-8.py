from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(1, 0), (0, 1)]

        @cache
        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            
            best = float('inf')
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    current = grid[r][c] + dfs(nr, nc)
                    best = min(best, current)
            return best

        res = dfs(0, 0)
        dfs.cache_clear()
        return res


