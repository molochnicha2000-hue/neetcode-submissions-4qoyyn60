class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        real = []
        cur = []
        N = len(nums)
        visit = [True] * N
        def dfs(i, visit):
            nonlocal res
            if len(cur) == N:
                if tuple(cur) not in res:
                    res.add(tuple(cur))
                    real.append(cur.copy())
                return 

            if i > N:
                return 

            for j in range(N):
                if visit[j]:
                    cur.append(nums[j])
                    visit[j] = False
                    dfs(j + 1, visit)
                    cur.pop()
                    visit[j] = True

            
        dfs(0, visit)
        return real