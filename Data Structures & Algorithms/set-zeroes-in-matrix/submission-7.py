class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        flag = False
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    grid[0][c] = 0
                    if r > 0:
                        grid[r][0] = 0
                    else:
                        flag = True
        for r in range(1, m):
            for c in range(1, n):
                if grid[0][c] == 0 or grid[r][0] == 0:
                    grid[r][c] = 0

        if grid[0][0] == 0:
            for r in range(m):
                grid[r][0] = 0

        if flag:
            for c in range(n):
                grid[0][c] = 0

        