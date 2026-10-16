class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c, visit):
            q = collections.deque([(r, c)])
            visit.add((r, c))
            while len(q) > 0:
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[r][c] <= grid[nr][nc] and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
        
        visit_pac = set()
        visit_atl = set()
        for c in range(cols):
            bfs(0, c, visit_pac)
            bfs(rows - 1, c, visit_atl)
        
        for r in range(rows):
            bfs(r, 0, visit_pac)
            bfs(r, cols - 1, visit_atl)

        res = []
        for r, c in visit_pac:
            if (r, c) in visit_atl:
                res.append([r, c])
        return res