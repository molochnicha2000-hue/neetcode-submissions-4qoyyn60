from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, s1, s2):
            if i == len(nums) : return s1 == s2
            return dfs(i + 1, s1 + nums[i], s2) | dfs(i + 1, s1, s2 + nums[i])
        return dfs(0, 0, 0)