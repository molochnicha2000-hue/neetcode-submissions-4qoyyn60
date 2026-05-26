class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best  = nums[0]
        N = len(nums)
        
        def dfs(i, cur):
            nonlocal best
            if i >= N:
                return
            
            for j in range(i, N):
                cur.append(nums[j])
                best = max(best, sum(cur))
            dfs(i + 1, [])
        dfs(0, [])
        return best
        