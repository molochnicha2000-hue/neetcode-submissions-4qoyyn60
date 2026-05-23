class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        rows, cols = len(text1), len(text2)
        grid = [[0] * (cols + 1) for _ in range(rows + 1)]

    
        res = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if text1[r] == text2[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r][c + 1], grid[r + 1][c]) 
                res = max(res, grid[r][c])
        print(grid)
        return res