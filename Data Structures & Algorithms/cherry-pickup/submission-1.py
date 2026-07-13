class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == -1:
            return 0
        if N == 1:
            return grid[0][0] 
        d_right = [(1, 0), (0, 1)]
        d_left = [(-1, 0), (0, -1)]

        dp1 = {}
        dp2 = {}

        def convert(grid):
            res = tuple(tuple(c) for c in grid)
            return res

        def dfs1(r, c, grid):
            if r == 0 and c == 0:
                return (0, True)

            co = convert(grid)
            if (r, c, co) in dp2:
                return dp2[(r, c, co)]
            
            best = 0
            flag = False
            for dr, dc in d_left:
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != -1:
                    current_res, current_b = dfs1(nr, nc, grid)
                    if current_b:
                        flag = True
                        best = max(best, grid[nr][nc] + current_res)

            dp2[(r, c, co)] = (best, flag)
            return (best, flag)

        def dfs(r, c, grid):
            if r == N - 1 and c == N - 1:
                current_res, current_b = dfs1(N - 1, N - 1, grid)
                if current_b:
                    return current_res
                return float("-inf")
            
            co = convert(grid)
            if (r, c, co) in dp1:
                return dp1[(r, c, co)]

            best = float("-inf")
            for dr, dc in d_right:
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != -1:
                    t = grid[nr][nc]
                    grid[nr][nc] = 0
                    best = max(best, t + dfs(nr, nc, grid))
                    grid[nr][nc] = t
            dp1[(r, c, co)] = best
            return best
        
        res = dfs(0, 0, grid)
        if res == float("-inf"):
            return 0
        return res
        
            





