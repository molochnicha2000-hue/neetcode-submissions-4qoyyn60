class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0
        for r in range(rows):
            for c in range(cols):
                cur = 4
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = dr + r, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            cur -= 1
                            
                    #print(cur, r, c)
                    res += cur
                    
        #print(grid)
        return res