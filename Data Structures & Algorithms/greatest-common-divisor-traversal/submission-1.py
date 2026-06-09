import math
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)
        adg = [[] for i in range(N)]
        for i in range(N):
            cur = nums[i]
            for j in range(i + 1, N):
                if math.gcd(cur, nums[j]) > 1:
                    adg[i].append(j)
                    adg[j].append(i)
                
        visit = [False] * N
        def dfs(node):
            visit[node] = True
            
            for j in adg[node]:
                if not visit[j]:
                    dfs(j)
            
        dfs(0)
        for node in visit:
            if not node:
                return False
        return True
        
