class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = float("-inf")
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c, amount):
            q = collections.deque([(r, c)])           
            grid[r][c] = 0
            camount = amount
            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc

                    if (nr < 0 or nc < 0 or nr == rows or nc == cols or
                        grid[nr][nc] == 0):
                        continue

                    grid[nr][nc] = 0
                    camount += 1
                    q.append((nr, nc))
            return camount


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c, 1))
        return res if res != float("-inf") else 0

        