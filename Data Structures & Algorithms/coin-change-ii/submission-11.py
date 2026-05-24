class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        res = 0
        dp = [[-1] * (amount + 1) for _ in range(N)]
        def dfs(i, curAmount):
            if curAmount == amount:                    
                return 1
            
            if i >= N or curAmount > amount:
                return 0

            if dp[i][curAmount] != -1:
                return dp[i][curAmount]

            
            take = dfs(i, curAmount + coins[i])
      
            skip =  dfs(i + 1, curAmount)
            dp[i][curAmount] = take + skip
            return take + skip
        
        return dfs(0, 0)
        
        return dp[0][0]