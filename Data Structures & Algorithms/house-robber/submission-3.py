from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(i, can):
            if i == N:
                return 0
            
            best = dfs(i + 1, True)
            if can:
                current = nums[i] + dfs(i + 1, False)
                best = max(best, current)
            return best
        
        res = dfs(0, True)
        return res
        