class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        l, r = 0, N - 1
        while l < r:
            for i in range(r - l):
                t, b = l, r

                matrix[t][l + i], matrix[t + i][r], matrix[b][r - i], matrix[b - i][l] = matrix[b - i][l], matrix[t][l + i], matrix[t + i][r], matrix[b][r - i]
            l += 1
            r -= 1