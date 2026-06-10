class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x : len(x))
        rows, cols = len(strs), len(strs[0])

        res = ""
        for c in range(cols):
            for r in range(rows - 1):
                if strs[r][c] != strs[r + 1][c]:
                    return res
            res += str(strs[0][c])
        return res
