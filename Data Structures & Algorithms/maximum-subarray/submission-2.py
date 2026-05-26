class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        dp = [[None] * 2 for i in range(N)]
        def dfs(i, flag):
            if i == N - 1:
                return max(0, nums[i]) if flag else nums[i]

            if dp[i][flag] != None:
                return dp[i][flag]
            
            if flag:
                dp[i][flag] = max(0, nums[i] + dfs(i + 1, True))
            else:
                dp[i][flag] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            return dp[i][flag]

        return dfs(0, False)
        
        