from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        @cache
        def dfs(r, c):
            best = 0
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    current = 1 + dfs(nr, nc)
                    best = max(best, current)
            return best
        
        best = 0
        for r in range(rows):
            for c in range(cols):
                best = max(best, 1 + dfs(r, c))
        return best