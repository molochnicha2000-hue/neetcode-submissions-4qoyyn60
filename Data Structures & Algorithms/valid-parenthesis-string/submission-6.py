class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[-1] == "(":
            return False

        N = len(s)
        dp = [[False] * (N + 1) for i in range(N + 1)]
        dp[N][0] = True

        for i in range(N - 1, -1, -1):
            for j in range(N):
                if s[i] == "*":
                    dp[i][j] = dp[i][j] or dp[i + 1][j + 1]
                    if j > 0:
                        dp[i][j] |= dp[i + 1][j - 1]
                    dp[i][j] |= dp[i + 1][j]
                else:
                    if s[i] == "(":
                        dp[i][j] |= dp[i + 1][j + 1]
                    else:
                        if j > 0:
                            dp[i][j] |= dp[i + 1][j - 1]
        return dp[0][0]