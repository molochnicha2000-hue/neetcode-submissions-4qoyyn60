from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def dfs(i, can_buy):
            if i >= N:
                return 0
            
            best = dfs(i + 1, can_buy)
            if can_buy:
                cur = -prices[i] + dfs(i + 1, False)
            else:
                cur = prices[i] + dfs(i + 2, True)
            return max(best, cur)

        r = dfs(0, True)
        return r