class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        N = len(nums)
        storage = []
        dp = {}    
        def dfs(amount):
            if amount == target:
                return 1

            if amount > target:
                return 0
            
            if (amount) in dp:
                return dp[(amount)]

            temp = 0
            for j in range(N):
                if amount + nums[j] <= target:
                    temp += dfs(amount + nums[j])

            dp[(amount)] = temp
            return temp
        # if set(cur) == 1 only 1 way
        # else count += len(cur)
        res = dfs(0)
        return res
        