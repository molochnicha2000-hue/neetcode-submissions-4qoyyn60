class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float("inf")] * (N)
        dp[N - 1] = 0

        for i in range(N - 1, -1, -1):
            cur = nums[i]
            for j in range(cur + 1):
                if i + j < N:
                    dp[i] = min(dp[i], dp[i + j] + 1)
                
                if i + j < N and j <= cur:
                    dp[i] = min(dp[i], dp[i + j] + 1)
        return dp[0]