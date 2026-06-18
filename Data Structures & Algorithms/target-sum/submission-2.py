class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = {}
        def dfs(i, cur):
            if cur == target and i == N:
                return 1

            if i >= N:
                return 0

            if (i, cur) in dp:
                return dp[(i, cur)]

            temp = dfs(i + 1, cur - nums[i]) + dfs(i + 1, cur + nums[i])
            dp[(i, cur)] = temp
            return temp

        res = dfs(0, 0)
        #print(dp)
        return res
