class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        N = len(nums)
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for a in range(1, target + 1):
            for n in range(N - 1, -1, -1):
                if a - nums[n] >= 0:
                    dp[a] += dp[a - nums[n]]
                    count += dp[a]
        #print(count, dp)
        return dp[target]