class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        directins = [(1, 0), (0, 1)]
        dp = [[0] * (cols + 1) for i in range(rows + 1)]
        dp[rows - 1][cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                if r == rows - 1 and c == cols - 1:
                    continue
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        #print(dp)
        return dp[0][0]

        