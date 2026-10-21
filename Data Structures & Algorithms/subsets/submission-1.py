class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []; n = len(nums)
        def dfs(i, cur):
            if i == n : self.res.append(cur[:]); return
            dfs(i + 1, cur); dfs(i + 1, cur + [nums[i]])
        dfs(0, [])
        return self.res