class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False] * n
        def dfs(node, prev):
            if visit[node] : return False
            visit[node] = True
            for nei in adj[node]:
                if nei == prev : continue
                if not dfs(nei, node) : return False
            return True
        ans = dfs(0, -1)
        return ans and all(visit)