class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #coins = 0
        N = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        
        dp = {}
        def dfs(nums):
            if len(nums) == 2:
                return 0

            if tuple(nums) in dp:
                return dp[tuple(nums)]

            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(nums[:i] + nums[i + 1:])
                maxCoins = max(maxCoins, coins)
            dp[tuple(nums)] = maxCoins
            return maxCoins
        return dfs(nums)

        