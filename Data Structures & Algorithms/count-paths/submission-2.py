class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-2] = 1
        # print(dp)
        for _ in range(m):
            ndp = [0] * (n + 1)
            for c in range(n - 1, -1, -1):
                ndp[c] = dp[c] + ndp[c + 1]
            dp = ndp
            # print(dp)
        return dp[0]