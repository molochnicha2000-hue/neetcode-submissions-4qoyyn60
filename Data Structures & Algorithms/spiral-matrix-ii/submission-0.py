class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        grid = [[0] * N for _ in range(N)]

        def fill(left, right, top, bottom, val):
            if left > right or top > bottom:
                return
            
            for c in range(left, right + 1):
                grid[top][c] = val
                val += 1
            top += 1

            for r in range(top, bottom + 1):
                grid[r][right] = val
                val += 1
            right -= 1

            for c in range(right, left - 1, -1):
                grid[bottom][c] = val
                val += 1
            bottom -= 1

            for r in range(bottom, top - 1, -1):
                grid[r][left] = val
                val += 1
            left += 1

            fill(left, right, top, bottom, val)
        
        fill(0, N - 1, 0, N - 1, 1)
        return grid
            