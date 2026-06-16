class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = {}
        def dfs(curSum):
            if curSum == n:
                return 1
            if curSum > n:
                return float("-inf")
            if curSum in dp:
                return dp[curSum]
            best = float("-inf")
            for num in range(2, n):
                best = max(best, num * dfs(curSum + num))
            dp[curSum] = best
            return best
        
        res = dfs(0)
        return res
        