class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        N = len(candidates)
        cur = []
        
        def dfs(i):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            
            if sum(cur) > target or i >= N:
                return

            prev = -1
            for j in range(i, N):
                if candidates[j] == prev:
                    continue
                cur.append(candidates[j])
                dfs(j + 1)        
                cur.pop()           
                #dfs(i + 1)
                prev = candidates[j]
        dfs(0)
        return res        