class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        N = len(cost)

        def dfs(i):
            if i >= N:
                return 0
            
            if i in dp:
                return dp[i]
            
            cur = cost[i] + min(dfs(i + 1), dfs(i + 2))
            dp[i] = cur
            return dp[i]

        return min(dfs(0), dfs(1))        