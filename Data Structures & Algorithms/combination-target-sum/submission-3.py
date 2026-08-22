class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        self.res = []

        def dfs(current, arr, i):
            if current == target:
                self.res.append(arr)
                return
            if i == N or current > target:
                return 
            dfs(current, arr, i + 1)
            dfs(current + nums[i], arr + [nums[i]], i)
        dfs(0, [], 0)
        return self.res