class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        count = 0
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                dp[l][r] = s[l] == s[r] and ((r - l) <= 1 or dp[l + 1][r - 1])
                count += dp[l][r]
        
        return count