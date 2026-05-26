class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        N = len(nums)
        dp = {}
        def dfs(i, amount):
            if amount == target:
                return True
            
            if i >= N or amount > target:
                return False
            
            if (i, amount) in dp:
                return dp[(i, amount)]
                
            v1 = dfs(i + 1, amount + nums[i])
            v2 = dfs(i + 1, amount)
            dp[(i, amount)] = (v1 or v2)
            return v1 or v2
        return dfs(0, 0)