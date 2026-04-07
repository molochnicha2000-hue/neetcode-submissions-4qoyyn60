from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [
                    [1, 0],
                    [-1, 0],
                    [0, 1],
                    [0, -1]
                ]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
                        #grid[nr][nc] = "0"

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res +=1
                    bfs(r,c)
        return res                   
        