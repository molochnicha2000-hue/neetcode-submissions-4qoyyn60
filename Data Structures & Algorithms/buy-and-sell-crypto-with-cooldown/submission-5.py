from functools import cache
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i, state):
            if i >= n : return 0
            return max(dfs(i + 1, state),
                (dfs(i + 2, False) + nums[i] if state else 0),
                (dfs(i + 1, True) - nums[i] if not state else 0)
            )
        return dfs(0, False)