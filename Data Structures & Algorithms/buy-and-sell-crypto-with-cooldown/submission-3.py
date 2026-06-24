class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}

        def dfs(i, cooldown): # True == I can't buy coins
            if i >= N:
                return 0

            if (i, cooldown) in dp:
                return dp[(i, cooldown)]

            total = dfs(i + 1, cooldown)
            if cooldown:
                for j in range(i, N):
                    total = max(total, dfs(j + 1, False) - prices[i])
            else:
                for j in range(i, N):
                    total = max(total, dfs(j + 2, True) + prices[i])
            dp[(i, cooldown)] = total
            return total
        res = 0
        for i in range(N):
            res = max(res, dfs(i + 1, False) - prices[i])
        return res