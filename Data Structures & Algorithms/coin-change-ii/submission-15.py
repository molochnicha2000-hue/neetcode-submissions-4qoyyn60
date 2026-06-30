class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        coins.sort()
        dp = [[-1] * N for _ in range(amount + 1)]
        
        def dfs(index, cur):
            if cur == 0:
                return 1
            if index >= N or cur < 0:
                return 0
            if dp[cur][index] != -1:
                return dp[cur][index]
            
            comb = dfs(index + 1, cur) + dfs(index, cur - coins[index])
            
            dp[cur][index] = comb
            return comb

        res = dfs(0, amount)
        
        return res