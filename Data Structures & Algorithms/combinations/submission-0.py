class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        arr = [i for i in range(1, n + 1)]

        N = len(arr) 
        cur = []
        def dfs(i):
            nonlocal res
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            for j in range(i, N):
                cur.append(arr[j])
                dfs(j + 1)

                cur.pop()
        dfs(0)
        return res
        