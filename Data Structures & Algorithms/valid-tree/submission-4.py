class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.visit = set()
        def dfs(node, prev):
            if node is None:
                return True
            if node in self.visit:
                return False
            self.visit.add(node)
            for nei in adj[node]:
                if nei == prev : continue
                if not dfs(nei, node) : return False
            return True
        if not dfs(0, -1) : return False
        return len(self.visit) == n