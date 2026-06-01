class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        dp = {}
        def dfs(x, k):
            if k == 0: return 1
            if x == 0: return 0

            temp = dfs(x, k // 2)
            res = temp * temp
            if k % 2 == 1:
                return res * x
            return res
        res = dfs(x, abs(n))
        if n >= 0:
            return res
        return 1 / res