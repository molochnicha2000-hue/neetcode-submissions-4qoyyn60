from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        @cache
        def dfs(i):
            if i == N:
                return 1
            
            best = dfs(i + 1) if s[i] != '0' else 0
            if i + 1 < N and ((s[i] == '2' and s[i + 1] in '0123456') or s[i] == '1'):
                current = dfs(i + 2)
                best += current
            return best
        res = dfs(0)
        return res