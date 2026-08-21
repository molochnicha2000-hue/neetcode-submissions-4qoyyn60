from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        sd = set(dictionary)

        @cache
        def dfs(i):
            if i == N:
                return 0

            best = 1 + dfs(i + 1)
            cur = ''
            for j in range(i, N):
                cur += s[j]
                if cur in sd:
                    c = dfs(j + 1)
                    best = min(best, c)
            return best

        return dfs(0)