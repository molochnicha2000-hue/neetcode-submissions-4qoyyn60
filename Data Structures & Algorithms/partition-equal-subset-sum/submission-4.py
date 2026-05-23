class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        N = len(nums)
        target = sum(nums) // 2
        dp = [[-1] * (target + 1) for _ in range(N + 1)]

        def dfs(i, cur1):
            if sum(cur1) == target:
                return True

            if i == N or sum(cur1) > target:
                return False

            need = target - sum(cur1)
            if dp[i][need] != -1:
                return dp[i][need]

            cur1.append(nums[i])
            v1 = dfs(i + 1, cur1)
            cur1.pop()

            v2 = dfs(i + 1, cur1)

            res = (v1 or v2)    
            dp[i][need] = res 
            return res
        
        return dfs(0, [])


        