class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(1, 0), (0, 1)]
        grid = [[0] * (n + 1) for i in range(m + 1)]
        # m - rows
        # n - cols
        grid[m - 1][n - 1] = 1

        #print(grid)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                grid[r][c] = grid[r + 1][c] + grid[r][c + 1] + grid[r][c]

        #print(grid) 
        return grid[0][0]