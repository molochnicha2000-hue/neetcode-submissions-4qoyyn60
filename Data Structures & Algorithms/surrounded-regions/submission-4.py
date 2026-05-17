class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            q = collections.deque([(r, c)])
            board[r][c] = "T"
            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (nr < 0 or nc < 0 or 
                        nr == rows or nc == cols or board[nr][nc] != "O"):
                        continue

                    board[nr][nc] = "T"
                    q.append((nr, nc))


        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
        
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)
        print(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
        
        