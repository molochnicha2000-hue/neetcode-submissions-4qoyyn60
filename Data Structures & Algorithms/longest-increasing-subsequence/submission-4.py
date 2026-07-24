from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(i, prev):
            if i == N:
                return 0
            
            best = dfs(i + 1, prev)
            if prev < nums[i]:
                c = 1 + dfs(i + 1, nums[i])
                best = max(best, c)
            return best
        
        res = dfs(0, float('-inf'))
        dfs.cache_clear()
        return res
