class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = nums
        N = len(nums)
        def dfs(ind, nums):
            if ind == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(ind, N):
                cur[ind], cur[i] = cur[i], cur[ind] 
                dfs(ind + 1, nums)
                cur[ind], cur[i] = cur[i], cur[ind] 
        dfs(0, nums)            
        return res
        
        