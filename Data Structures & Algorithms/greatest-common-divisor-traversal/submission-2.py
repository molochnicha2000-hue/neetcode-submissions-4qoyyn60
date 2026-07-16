class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)
        adj = collections.defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                c = math.gcd(nums[i], nums[j])
                if c > 1:
                    adj[i].append(j)
                    adj[j].append(i)

        visit = [False] * N
        def dfs(node):
            if visit[node]:
                return

            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
        dfs(0)
        for i in range(N):
            if not visit[i]:
                return False
        
        return True
            