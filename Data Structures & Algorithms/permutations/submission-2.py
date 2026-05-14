class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        cur = []
        visited = [False] * N 
        def dfs():
            if len(cur) == N:
                res.append(cur.copy())
                return
            
            for i in range(N):
                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    dfs()

                    cur.pop()
                    visited[i] = False
        dfs()
        return res