class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = [[None] * rows for _ in range(cols)]


        for r in range(cols):
            for c in range(rows):
                res[r][c] = matrix[c][r]
        return res