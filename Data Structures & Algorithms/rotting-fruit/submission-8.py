class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque(); total = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    total += 1
        
        ans = 0
        while len(q) > 0 and total > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        total -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            ans += 1
        return ans if total == 0 else -1