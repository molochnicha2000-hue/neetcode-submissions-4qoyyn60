class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posD = set() # (r + c) - const
        negD = set() # (r - c) - const

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(i)for i in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (r + c) in posD or (r - c) in negD or c in col:
                    continue
                
                posD.add((r + c))
                negD.add((r - c))
                col.add(c)
                board[r][c] = "Q"
                dfs(r + 1)

                posD.remove((r + c))
                negD.remove((r - c))
                col.remove(c)
                board[r][c] = "."
        dfs(0)
        return res
                

                
