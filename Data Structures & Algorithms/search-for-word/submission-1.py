class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[i] or 
                (r, c) in visit):
                return False
            i += 1
            if i == len(word):
                return True 
                
            visit.add((r, c))
            temp = (dfs(r + 1, c, i) or
                    dfs(r - 1, c, i) or
                    dfs(r, c + 1, i) or
                    dfs(r, c - 1, i))
            visit.remove((r,c))
            return temp

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False