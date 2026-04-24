class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        # chech rows
        for r in range(rows):
            rowsSet = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowsSet:
                    return False
                rowsSet.add(board[r][c])
        
        #check cols -> up - bottom

        for c in range(cols):
            colsSet = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colsSet:       
                    return False
                
                colsSet.add(board[r][c])

        # check 3 x 3 areas

        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
        