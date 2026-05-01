class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == target:
                    return True
        return False