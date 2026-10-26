class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        rows, cols = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, r, c):
            if i == len(word) : return True
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr, nc) not in visit and grid[nr][nc] == word[i]):
                    visit.add((nr, nc))
                    if dfs(i + 1, nr, nc) : return True
                    visit.remove((nr, nc))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == word[0]:
                    visit = set([(r, c)])
                    if dfs(1, r, c):
                        return True
        return False

