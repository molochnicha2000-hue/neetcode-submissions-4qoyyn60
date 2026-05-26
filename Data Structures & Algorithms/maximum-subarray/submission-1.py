class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best  = nums[0]
        N = len(nums)
        
        def dfs(i):
            nonlocal best
            if i >= N:
                return
            cur = 0
            for j in range(i, N):
                cur += nums[j]
                best = max(best, cur)
            dfs(i + 1)
        dfs(0)
        return best
        