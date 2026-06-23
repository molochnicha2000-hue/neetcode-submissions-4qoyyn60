class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        coins.sort()

        dp = [[0] * (amount + 1) for i in range(N + 1)]
        for c in range(N + 1):
            dp[c][0] = 1
        for index in range(N - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[index]:
                    dp[index][a] = dp[index + 1][a]
                    dp[index][a] += dp[index][a - coins[index]]
        return dp[0][amount]

