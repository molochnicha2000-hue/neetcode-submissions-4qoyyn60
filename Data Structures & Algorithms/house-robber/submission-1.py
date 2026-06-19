class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}

        def dfs(i, canrob):
            if i >= N:
                return 0

            if (i, canrob) in dp:
                return dp[(i, canrob)]

            best = 0
            if canrob:
                best = nums[i] + dfs(i + 1, False)

            best = max(best, dfs(i + 1, True), dfs(i + 1, False))
            dp[(i, canrob)] = best
            return best

        res = max(dfs(0, True), dfs(0, False))
        return res
        
            
            