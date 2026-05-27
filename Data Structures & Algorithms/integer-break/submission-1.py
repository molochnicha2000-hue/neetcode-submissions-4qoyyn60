class Solution:
    def integerBreak(self, n: int) -> int:
        # k >= 2
        # res is the product of integers
        cur = []
        res = 0
        dp = {}

        def dfs(amount):
            if amount == n:
                return 1

            if amount > n:
                return 0

            if amount in dp:
                return dp[amount]
            temp = 0
            for j in range(1, n):
                if amount + j <= n:
                    temp = max(temp, dfs(amount + j) * j)
            dp[amount] = temp
            return temp
        return dfs(0)
        