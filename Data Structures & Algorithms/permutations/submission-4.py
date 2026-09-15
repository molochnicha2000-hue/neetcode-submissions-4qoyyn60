class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(cur, mask):
            if mask == ((1 << len(nums)) - 1):
                self.ans.append(cur)
                return
            for i in range(len(nums)):
                if mask & (1 << i) == 0:
                    dfs(cur + [nums[i]], mask | (1 << i))
        dfs([], 0)
        return self.ans