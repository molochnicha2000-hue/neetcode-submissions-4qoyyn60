from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins); coins.sort()
        @cache
        def dfs(i, amount):
            if amount == 0 : return 1
            if i == n or amount < 0 : return 0
            return dfs(i + 1, amount) + dfs(i, amount - coins[i])
        return dfs(0, amount)