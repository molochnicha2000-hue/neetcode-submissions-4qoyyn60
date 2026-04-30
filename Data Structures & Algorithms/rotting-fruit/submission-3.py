class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                    nr, nc = r + dr, c + dc
                
                    if  (nr >= 0 and nc >= 0 and 
                        nr < rows and nc < cols and 
                        grid[nr][nc] == 1): 

                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1
        