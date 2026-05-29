class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * (N)
        dp[N - 1] = True

        for i in range(N - 1, -1, -1):
            cur = nums[i]
            for step in range(cur + 1):
                if step == 0:
                    continue
                if i + step >= N - 1:
                    dp[i] = True
                    break
                dp[i] = dp[i] or dp[i + step]
                if dp[i]:
                    break
        return dp[0]