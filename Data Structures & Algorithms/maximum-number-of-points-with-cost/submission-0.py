class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = {}
        def dfs(r, c):
            if r == rows - 1:
                return points[r][c]
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            best = 0
            for nc in range(cols):
                best = max(best, points[r][c] + dfs(r + 1, nc) - abs(c - nc))
            
            dp[(r, c)] = best
            return best
        res = 0
        for c in range(cols):
            res = max(res, dfs(0, c))
        return res