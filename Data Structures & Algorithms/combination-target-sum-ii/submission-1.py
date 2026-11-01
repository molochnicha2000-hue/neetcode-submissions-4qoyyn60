class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort(); self.ans = []; self.visit = [False] * n

        def dfs(i, A, cur):
            if cur == target : 
                self.ans.append(A[:])
                return
            if cur > target or i == n:
                return
            dfs(i + 1, A, cur)
            if i >= 1 and nums[i - 1] == nums[i] and self.visit[i - 1] is False:
                return
            self.visit[i] = True
            dfs(i + 1, A + [nums[i]], cur + nums[i])
            self.visit[i] = False
        dfs(0, [], 0)
        return self.ans

            
        