class Solution:
    def maxProfit(self, A: List[int]) -> int:
        n = len(A)
        dp = [[-1] * 2 for _ in range(n)]
        def dfs(i, flag):
            if i >= n:
                return 0
            if dp[i][flag] == -1:             
                dp[i][flag] = max(dfs(i + 1, flag),
                    (-A[i] + dfs(i + 1, flag ^ 1) if not flag else -math.inf),
                    (A[i] + dfs(i + 2, flag ^ 1) if flag else -math.inf)
                )
            return dp[i][flag]
        return dfs(0, 0)