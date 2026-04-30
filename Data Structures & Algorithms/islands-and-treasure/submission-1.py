class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c, steps):
            visit = set()
            q = collections.deque()
            q.append((r, c, steps))
            visit.add((r, c))
            while q:
                qr, qc, qsteps = q.popleft()
                if grid[qr][qc] == 0:
                    return qsteps

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc

                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in visit or grid[nr][nc] == -1):
                        continue

                    visit.add((nr, nc))
                    q.append((nr, nc, qsteps + 1))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c, 0) # maybe (r, c, 1)