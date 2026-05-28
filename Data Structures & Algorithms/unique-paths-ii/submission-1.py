class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        directins = [(1, 0), (0, 1)]
        dp = {}
        def dfs(r, c):
            if r == rows - 1 and c ==  cols - 1:
                return 1

            if r >= rows or c >= cols:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]

            res = dfs(r + 1, c) + dfs(r, c + 1)
            dp[(r, c)] = res
            return res
        return dfs(0, 0)