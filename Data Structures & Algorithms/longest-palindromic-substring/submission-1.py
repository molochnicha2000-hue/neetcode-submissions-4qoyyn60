class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * (N + 1) for _ in range(N + 1)]

        dp[N][N] = True
        resLen = 1
        res = s[0]
        for i in range(N - 1, -1, -1):

            for j in range(i, N):
                if s[i] == s[j] and (dp[i + 1][j - 1] or (j - i <= 2)):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resLen = (j - i + 1)
                        res = s[i : j + 1]
        #l, r = res
        #print(dp)
        return res
                        
