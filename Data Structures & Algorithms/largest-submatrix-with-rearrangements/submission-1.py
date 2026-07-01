class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        prev_work = [0] * cols

        for r in range(rows):
            work = matrix[r][::]
            for c in range(cols):
                if work[c] > 0:
                    work[c] += prev_work[c]

            cur = sorted(work, reverse = True)
            for i in range(cols):
                res = max(res, (i + 1) * cur[i])
            
            prev_work = work
        return res
            

        
        