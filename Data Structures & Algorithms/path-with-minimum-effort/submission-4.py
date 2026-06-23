class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()
        while heap:
            count, x, y = heapq.heappop(heap)
            if x == rows - 1 and y == cols - 1:
                return count

            if (x, y) in visit:
                continue
                
            visit.add((x, y))
            for dx, dy in d:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols:
                    new = max(count, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(heap, (new, nx, ny))
        return 0