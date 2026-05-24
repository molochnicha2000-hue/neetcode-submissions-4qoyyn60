class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(N)]
        
        curList = []
        def dfs(i, curAmount):
            if curAmount == amount:            
                return 1
            
            if i >= N or curAmount > amount:
                return 0
            
            if dp[i][curAmount] != -1:
                return dp[i][curAmount]
            
            skip = dfs(i + 1, curAmount)
            
            take = dfs(i, curAmount + coins[i])

            dp[i][curAmount] = take + skip
            return dp[i][curAmount]

        return dfs(0, 0)
        
        