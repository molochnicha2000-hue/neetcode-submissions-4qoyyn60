class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = set()
        state = [False] * N
        def dfs(cur):
            nonlocal res, state
            if len(cur) == N:
                res.add(tuple(cur))
                return
            
            for index, val in enumerate(nums):
                if not state[index]:
                    state[index] = True
                    dfs(cur + [val])
                    state[index] = False
        dfs([])
        return [list(cur) for cur in res]