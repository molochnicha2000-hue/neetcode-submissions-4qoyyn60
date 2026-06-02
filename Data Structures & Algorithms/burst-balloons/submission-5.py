class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]

        dp = {}
        def dfs(cur):
            if len(cur) <= 2:
                return 0

            if tuple(cur) in dp:
                return dp[tuple(cur)]

            best = float("-inf")
            for j in range(1, len(cur) - 1):
                temp = cur[j - 1] * cur[j] * cur[j + 1]
                best = max(best, dfs(cur[:j] + cur[j + 1:]) + temp)
            dp[tuple(cur)] = best
            return best
        res = dfs(nums)
        return res
            