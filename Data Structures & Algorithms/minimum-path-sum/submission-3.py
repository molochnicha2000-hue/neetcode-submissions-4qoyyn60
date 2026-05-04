class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # heapq

        rows, cols = len(grid), len(grid[0])
        directions = [
            (1, 0),
            (0, 1)
        ]
        
        # only down and right
        heapi = [(grid[0][0], 0, 0)]
        visit = set()
        while heapi:
            amount, r, c = heapq.heappop(heapi)
            if (r, c) in visit:
                continue
                
            visit.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return amount

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr == rows or nc == cols:
                    continue
                heapq.heappush(heapi, (amount + grid[nr][nc], nr, nc))
