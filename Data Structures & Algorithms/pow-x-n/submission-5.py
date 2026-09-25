from functools import cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        x = (1 / x if n < 0 else x)
        @cache
        def dfs(depth):
            if depth == 0:
                return 1
            return dfs(depth // 2) * dfs(depth // 2) * (x if depth % 2 == 1 else 1)
        r = dfs(abs(n))
        return r
