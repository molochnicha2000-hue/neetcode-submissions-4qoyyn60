class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # if grid[r][c] >= grid[nr][nc] so water flow to this posit
        # we want to find all points where water can go to atl and pac
        pacif = [[False] * cols for r in range(rows)]
        atl = [[False] * cols for r in range(rows)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nc < 0 or nr == rows or nc == cols
                        or ocean[nr][nc] or heights[nr][nc] < heights[r][c]):
                        continue
    
                    q.append((nr, nc))


        pacific, atlantic = [], []
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        bfs(pacific, pacif)
        bfs(atlantic, atl)

        for r in range(rows):
            for c in range(cols):
                if pacif[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
