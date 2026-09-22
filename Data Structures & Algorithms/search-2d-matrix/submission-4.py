class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        l, r = 0, rows - 1
        need = None
        while l <= r:
            m = (l + r) // 2
            if grid[m][0] <= target <= grid[m][-1]:
                need = m
                break
            if grid[m][-1] > target:
                r = m - 1
            else:
                l = m + 1
        if need is None : return False
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if grid[need][m] == target:
                return True
            if grid[need][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False