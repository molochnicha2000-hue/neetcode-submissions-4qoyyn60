class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        dp = [float("-inf")] * (N + 1)
        dp[N] = 0

        for i in range(N - 1, -1, -1):
            total = 0
            for j in range(i, min(N, i + 3)):
               total += stoneValue[j]
               dp[i] = max(dp[i], total - dp[j + 1])

        res = dp[0] 
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"
