class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        tries = (numRows - 1) * 2
        for i in range(numRows):
            for j in range(i, len(s), tries):
                res += s[j]
                if i > 0 and i < numRows - 1 and j + tries - 2 * i < len(s):
                    res += s[j + tries - 2 * i] 
        return res
        