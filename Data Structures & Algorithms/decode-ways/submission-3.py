class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        N = len(s)
        dp = [0]  * N

        def dfs(i):
            if i == N:
                return 1

            if i > N or s[i] == "0":
                return 0

            if dp[i] != 0:
                return dp[i] 
            cur = dfs(i + 1) if i + 1 <= N else 0
            right = 0
            if i + 2 <= N and 1 <= int(s[i:i + 2]) < 27:
                right = dfs(i + 2) 
            
            dp[i] = cur + right
            return dp[i]
        dfs(0)
        return dp[0]