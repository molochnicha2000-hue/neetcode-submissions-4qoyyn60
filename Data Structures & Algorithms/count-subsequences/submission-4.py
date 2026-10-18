from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s); target = len(t)
        @cache
        def dfs(i, j):
            if j == target : return 1
            if i == n : return 0
            return dfs(i + 1, j) + (dfs(i + 1, j + 1) if s[i] == t[j] else 0)
        return dfs(0, 0)