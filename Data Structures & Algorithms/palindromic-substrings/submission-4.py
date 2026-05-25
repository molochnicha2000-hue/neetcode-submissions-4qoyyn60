class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False] * (N + 1) for i in range(N + 1)]

        res = 0
        for r in range(N - 1, -1, -1):
            for c in range(r, N):
                if s[r] == s[c] and (c - r <= 2 or dp[r + 1][c - 1]):
                    dp[r][c] = True
                    res += 1
                
        #print(dp)
        return res
        

        