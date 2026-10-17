class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(arr):
            if len(arr) == 2 : return 0
            tu = tuple(arr)
            if tu not in dp:           
                dp[tu] = max(
                    dfs(arr[:i] + arr[i + 1:]) + arr[i - 1] * arr[i] * arr[i + 1]
                    for i in range(1, len(arr) - 1)
                )
            return dp[tu]
        return dfs(nums)

