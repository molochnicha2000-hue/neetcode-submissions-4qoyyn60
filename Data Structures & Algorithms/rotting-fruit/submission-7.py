class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        q = collections.deque()
        fruits = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 : q.append((r, c))
                fruits += grid[r][c] == 1
        
        time = 0
        while len(q) > 0 and fruits > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fruits -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        if fruits == 0 : return time
        return -1