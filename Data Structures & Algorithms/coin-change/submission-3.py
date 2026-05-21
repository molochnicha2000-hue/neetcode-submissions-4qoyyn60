class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        
        dp = {}
        def dfs(amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            res = float("inf")
            for c in range(N):
                if amount - coins[c] >= 0:
                    res = min(res, dfs(amount - coins[c]) + 1)
            dp[amount] = res
            return dp[amount]

        res = dfs(amount)
        return res if res != float("inf") else -1