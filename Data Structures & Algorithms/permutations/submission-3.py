class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = set()

        def dfs(visit, current):
            if len(visit) == N:
                res.add(tuple(current))
                return
            
            for i in range(N):
                if i not in visit:
                    visit.add(i)
                    dfs(visit, current + [nums[i]])
                    visit.remove(i)
        
        dfs(set(), [])
        r = [list(x) for x in res]
        return r