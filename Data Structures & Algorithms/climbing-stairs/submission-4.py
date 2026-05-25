class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        #dp[n][n] = 1
        dp[n] = 1
        #print(dp)
        for i in range(n - 1, -1, -1):
            v1 = dp[i + 1] if i + 1 <= n else 0
            v2 = dp[i + 2] if i + 2 <= n else 0
            dp[i] = v1 + v2

        #print(dp)
        return dp[0] 