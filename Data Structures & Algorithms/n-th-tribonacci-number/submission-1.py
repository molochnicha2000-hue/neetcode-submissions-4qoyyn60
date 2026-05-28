class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def dfs(amount):
            if amount <= 2:
                return 1 if amount != 0 else 0
            
            if amount in dp:
                return dp[amount]
                
            res = dfs(amount - 3) + dfs(amount - 2) + dfs(amount - 1)
            dp[amount] = res
            return res
        return dfs(n)