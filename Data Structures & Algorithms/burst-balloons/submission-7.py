from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        @cache
        def dfs(l, r):
            if l > r : return 0
            best = 0
            for k in range(l, r + 1):
                left = dfs(l, k - 1)
                right = dfs(k + 1, r)
                best = max(best, 
                nums[l - 1] * nums[k] * nums[r + 1] + (left + right)
                )
            return best
        return dfs(1, n - 2)
