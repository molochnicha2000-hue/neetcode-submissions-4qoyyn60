import functools
inf = float('inf')
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        """
        @functools.cache
        def dfs(i):
            if i >= N - 1:
                return 0

            best = inf
            for j in range(1, nums[i] + 1):
                current = 1 + dfs(i + j)
                best = min(best, current)
            return best
        return dfs(0)
        """
        dp = [inf] * N
        dp[-1] = 0
        for i in range(N - 2, -1, -1):
            best = inf
            for j in range(1, nums[i] + 1):
                current = 1 + dp[min(N - 1, i + j)]
                best = min(best, current)
            dp[i] = best
        return dp[0]