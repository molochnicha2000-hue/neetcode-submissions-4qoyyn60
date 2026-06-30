class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        coins.sort()
        dp = [[0] * (N + 1) for _ in range(amount + 1)]

        for r in range(N + 1):
            dp[0][r] = 1
          
        for a in range(amount + 1):

            for i in range(N - 1, -1, -1):
                coin = coins[i]
                if a >= coin:
                    comb = dp[a][i + 1]
                    comb += dp[a - coin][i]
                    dp[a][i] = comb
        
        return dp[amount][0]