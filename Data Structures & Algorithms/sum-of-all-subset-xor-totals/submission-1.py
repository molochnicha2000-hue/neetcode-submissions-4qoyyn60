class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        
        def f(cur):
            res = 0
            for n in cur:
                res ^= n
            return res

        def dfs(i, cur):
            nonlocal res
            res += cur
            if i >= N:
                return
            for j in range(i, N):
                dfs(j + 1, cur ^ nums[j])
        dfs(0, 0)
        return res