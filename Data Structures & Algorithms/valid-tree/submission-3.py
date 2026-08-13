class Solution:
    def validTree(self, N: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.visit = [False] * N
        def dfs(node, prev):
            if self.visit[node]:
                return False

            self.visit[node] = True
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        if not all(c for c in self.visit):
            return False
        return True