class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        h = [(grid[0][0], 0, 0)]
        visit = [[math.inf] * cols for _ in range(rows)]
        while len(h) > 0:
            time, r, c = heapq.heappop(h)
            if visit[r][c] <= time:
                continue
            visit[r][c] = time
            if (r, c) == (rows - 1, cols - 1):
                return time
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    new = (grid[nr][nc] if grid[nr][nc] > time else time)
                    heapq.heappush(h, (new, nr, nc))