class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        self.visit = set()
        def dfs(cur, path):
            if cur in path : return False
            if cur in self.visit : return True
            path.add(cur)
            self.visit.add(cur)
            for nei in adj[cur]:
                if not dfs(nei, path) : return False
            path.remove(cur)
            return True
        
        for src in range(n):
            if not dfs(src, set()):
                return False
        return True