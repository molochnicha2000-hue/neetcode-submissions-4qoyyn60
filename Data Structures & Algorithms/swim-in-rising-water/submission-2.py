class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visit = set()
        h = [(grid[0][0], 0, 0)]
        while len(h) > 0:
            M, r, c = heapq.heappop(h)
            if (r, c) == (rows - 1, cols - 1) : return M
            if (r, c) in visit : continue
            else : visit.add((r, c))
            for dr, dc in d:
                nr = r + dr; nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(h, (max(M, grid[nr][nc]), nr, nc))
        """
        [[0,1,2,3,4],
        [24,23,22,21,5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10,9,8,7,6]]

        """
        return -1