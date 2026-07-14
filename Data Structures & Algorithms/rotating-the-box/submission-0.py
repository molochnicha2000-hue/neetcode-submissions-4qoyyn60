class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in range(rows):
            i = cols - 1
            for c in range(cols - 1, -1, -1): 
                if boxGrid[r][c] == "*":
                    i = c - 1     
                elif boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
        
        res = []
        for c in range(cols):
            cur = []
            for r in range(rows - 1, -1, -1):
                cur.append(boxGrid[r][c])
            res.append(cur)
        return res
