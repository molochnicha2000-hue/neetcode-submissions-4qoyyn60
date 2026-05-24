class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] * (N + 1) for i in range(amount + 1)]
        dp[0] = [1] * (N + 1)

        
        for cur in range(1, amount + 1):
            for i in range(N - 1, -1, -1):
                dp[cur][i] = dp[cur][i + 1]
                if cur - coins[i] < 0:
                    continue
                dp[cur][i] += dp[cur - coins[i]][i]
        return dp[amount][0] 