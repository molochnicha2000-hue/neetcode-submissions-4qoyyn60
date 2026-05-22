class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i] 

            LIS = 1
            for j in range(i + 1, N):
                if nums[j] > nums[i]:
                    LIS = max(LIS, dfs(j) + 1)
            dp[i] = LIS
            return dp[i]
        res = 1
        for i in range(N):
            res = max(res, dfs(i))
        return res