class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2 ** 31 - 1
        q = collections.deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while len(q) > 0:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > dist + 1:
                        grid[nr][nc] = dist + 1
                        q.append((nr, nc, dist + 1))
        """
        [4,-1,0,1]
        [3,2,1,-1],
        [1,-1,2,-1],
        [0,-1,3,4]
        """
        