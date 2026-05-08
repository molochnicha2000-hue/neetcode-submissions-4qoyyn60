class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = 0
        rows, cols = len(matrix), len(matrix[0])

        visit = {} # (r, c) : path
        def dfs(r, c, path, val):
            if (r < 0 or c < 0 or 
                c == cols or r == rows or
                matrix[r][c] <= val):
                return 0

            if (r, c) in visit:
                return visit[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, path + 1,  matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, path + 1,  matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, path + 1,  matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, path + 1,  matrix[r][c]))  
            visit[(r, c)] = res
            return res        

        #dfs(0, 0, 1, grid[0][0])
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visit:
                    longest = max(longest, 1 + visit[(r, c)])
                    continue
                print(dfs(r, c, 1, matrix[r][c]))
                #longest = max(longest, dfs(r, c, 1, matrix[r][c]))
                longest = max(longest, dfs(r, c, 1, float("-inf")))

        return longest



        for ind, path in visit.items():
            longest = max(longest, path)
        return longest