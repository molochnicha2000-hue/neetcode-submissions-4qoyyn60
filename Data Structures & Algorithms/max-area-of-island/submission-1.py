class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0


        def bfs(r, c):
            q = collections.deque([(r, c)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            res = 1
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        res += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur = bfs(r, c)
                    
                    res = max(cur, res)
        
        return res