class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for i in range(len(nums) + 1)]

        # rows (0 - n), cols (-inf : 0) and (0: +inf)

        dp[0][0] = 1
        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        print(dp)
        return dp[len(nums)][target]

        