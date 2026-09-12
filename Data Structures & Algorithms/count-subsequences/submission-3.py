from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(t) : return 1
            if i == len(s) : return 0
            return dfs(i + 1, j) + (dfs(i + 1, j + 1) if s[i] == t[j] else 0)
        return dfs(0, 0)