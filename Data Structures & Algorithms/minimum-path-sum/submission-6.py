class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visit = set()
        while heap:
            count, x, y = heapq.heappop(heap)
            if x == rows - 1 and y == cols - 1:
                return count
            
            if (x, y) in visit:
                continue
            visit.add((x, y))
            for dx, dy in [(0, 1), (1, 0)]:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols:
                    heapq.heappush(heap, (count + grid[nx][ny], nx, ny))
        
        return 1