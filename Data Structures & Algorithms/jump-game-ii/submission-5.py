class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {N - 1 : 0}

        def dfs(i):
            if i >= N - 1:
                return 0

            if i in dp:
                return dp[i]

            temp = float("inf")
            cur = nums[i]

            for step in range(1, cur + 1):
                if i + step < N:
                    temp = min(temp, dfs(i + step) + 1)
                if i + step < N and i + step <= cur:
                    temp = min(temp, dfs(i + step) + 1)
            dp[i] = temp
            return temp
        res = dfs(0)
        #print(dp)
        return res