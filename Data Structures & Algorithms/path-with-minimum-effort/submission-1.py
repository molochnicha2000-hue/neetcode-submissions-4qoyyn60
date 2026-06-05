class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        res = 0
        rows, cols = len(heights), len(heights[0])
        minH = [(0, 0, 0)]
        #heapq.heappush(minH, (0, 0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()
        while minH:
            diff, x, y = heapq.heappop(minH)
            if x == rows - 1 and y == cols - 1:
                return diff
            
            if (x, y) in visit:
                continue

            visit.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new = abs(heights[x][y] - heights[nx][ny])
                    heapq.heappush(minH, (max(diff, new), nx, ny))
        return -1
