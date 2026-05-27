class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        N = len(nums)
        storage = []
        dp = {}
        def dfs(i, amount):
            if amount == target:
                return 1

            if i >= N or amount > target:
                return 0
            
            if (i, amount) in dp:
                return dp[(i, amount)]

            temp = 0
            for j in range(N):
                if amount + nums[j] <= target:
                    temp += dfs(j, amount + nums[j])

            dp[(i, amount)] = temp
            return temp
        # if set(cur) == 1 only 1 way
        # else count += len(cur)
        res = dfs(0, 0)
        print(dp)
        return res
        