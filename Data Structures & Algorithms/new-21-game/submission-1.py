class Solution:
    def new21Game(self, N: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        
        total = 0
        for i in range(k, k + maxPts):
            total += 1 if i <= N else 0
        
        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = total / maxPts
            remove = 0
            if i + maxPts <= N:
                remove = dp.get(i + maxPts, 1)      
            total += dp[i] - remove
        return dp[0]