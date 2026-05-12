class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        fruits = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fruits += 1
        print(q)
        while q and fruits > 0:
            for i in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc

                    if (nr < 0 or nc < 0 or 
                        nr == rows or nc == cols or grid[nr][nc] != 1):
                        continue
                        
                    grid[nr][nc] = 2
                    fruits -= 1
                    q.append((nr, nc))
            time += 1   
        return time if fruits == 0 else -1