class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        dpc = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == "1":
                    dpc[r][c] = 1 + min(dpc[r + 1][c], dpc[r][c + 1], dpc[r + 1][c + 1])
                         
                    res = max(res, dpc[r][c]) 
        return res ** 2


