from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(s)
        target = len(t)

        @cache
        def dfs(i, j):
            if j == target:
                return 1
            if i == N:
                return 0

            best = dfs(i + 1, j)
            if s[i] == t[j]:
                current = dfs(i + 1, j + 1)
                best += current
            return best

        res = dfs(0, 0)
        return res