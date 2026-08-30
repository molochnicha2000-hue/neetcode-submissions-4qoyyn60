from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        @cache
        def dfs(i, j):
            if i == N1 or j == N2:
                return 0
            best = max(dfs(i + 1, j), dfs(i, j + 1))
            if text1[i] == text2[j]:
                best = max(best, 1 + dfs(i + 1, j + 1))
            return best
        return dfs(0, 0)